from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

from services.gmail_service import gmail_service
from services.ai_service import ai_service

from services.data_manager import data_manager

app = Flask(__name__)
CORS(app)

def _get_keys():
    return {
        "gemini_key": request.headers.get("X-Gemini-Key"),
        "client_id": request.headers.get("X-Google-Client-Id"),
        "client_secret": request.headers.get("X-Google-Client-Secret")
    }

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/api/labels', methods=['GET'])
def get_labels():
    keys = _get_keys()
    if not all([keys['client_id'], keys['client_secret']]):
        return jsonify({"error": "Google Credentials missing in headers"}), 400
    labels = gmail_service.get_labels_sync(keys['client_id'], keys['client_secret'])
    return jsonify(labels)

@app.route('/api/emails', methods=['GET'])
def get_emails():
    keys = _get_keys()
    if not all([keys['client_id'], keys['client_secret'], keys['gemini_key']]):
        return jsonify({"error": "Required credentials missing in headers"}), 400
        
    count = request.args.get('count', default=20, type=int)
    label = request.args.get('label')
    emails = gmail_service.get_emails_sync(keys['client_id'], keys['client_secret'], count, label=label, unread_only=True)
    
    if isinstance(emails, dict) and "error" in emails:
        return jsonify(emails), 500

    header_data = [{"id": e['id'], "subject": e.get('subject', ''), "from": e.get('from', '')} for e in emails]
    sensitivity = ai_service.classify_sensitivity(header_data, api_key=keys['gemini_key'])
    
    sensitive_ids = {s['id'] for s in sensitivity if s.get('sensitive')}
    
    for email in emails:
        if email['id'] in sensitive_ids:
            email['sensitive'] = True
            email['snippet'] = "[SENSITIVE CONTENT HIDDEN]"
        else:
            email['sensitive'] = False
            
    data_manager.save_emails(emails)
    return jsonify(emails)

@app.route('/api/tags', methods=['GET', 'POST', 'DELETE'])
def manage_tags():
    if request.method == 'GET':
        return jsonify(data_manager.get_tags())
    elif request.method == 'POST':
        tag = request.json.get('tag')
        return jsonify(data_manager.save_tag(tag))
    elif request.method == 'DELETE':
        tag = request.args.get('tag')
        return jsonify(data_manager.delete_tag(tag))

@app.route('/api/local-data', methods=['GET', 'DELETE'])
def local_data():
    if request.method == 'GET':
        return jsonify(data_manager.get_emails())
    elif request.method == 'DELETE':
        data_manager.clear_emails()
        return jsonify({"status": "cleared"})

@app.route('/api/generate-query', methods=['POST'])
def generate_query():
    keys = _get_keys()
    tags = request.json.get('tags', [])
    query = ai_service.generate_tag_query(tags, api_key=keys['gemini_key'])
    return jsonify({"query": query})

@app.route('/api/classify', methods=['POST'])
def classify():
    keys = _get_keys()
    data = request.json
    emails = data.get('emails', [])
    if not emails:
        return jsonify({"error": "No emails provided"}), 400
    
    classification = ai_service.classify_emails(emails, api_key=keys['gemini_key'])
    return jsonify(classification)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
