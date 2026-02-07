import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

class AIService:
    def __init__(self):
        self.model = None
        self.current_key = None

    def _setup_model(self, api_key):
        if api_key and api_key != self.current_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            self.current_key = api_key
        return self.model

    def classify_sensitivity(self, email_headers, api_key=None):
        """
        Check if emails are sensitive based on Subject/From.
        """
        model = self._setup_model(api_key)
        if not model: return [{"id": e['id'], "sensitive": False} for e in email_headers]
        
        prompt = f"""
        Analyze these email headers and determine if they are sensitive (e.g., banking, healthcare, private credentials, legal).
        Return a JSON list of objects with "id" and "sensitive" (boolean).
        
        Headers:
        {json.dumps(email_headers, indent=2)}
        """
        try:
            response = self.model.generate_content(prompt)
            content = self._extract_json(response.text)
            return content
        except:
            return [{"id": e['id'], "sensitive": False} for e in email_headers]

    def recommend_tags(self, email_data, available_tags, api_key=None):
        """
        Assign multiple tags to each email from the available list.
        """
        model = self._setup_model(api_key)
        if not model: return []
        
        prompt = f"""
        Categorize these emails using the following available tags: {available_tags}.
        Each email can have multiple tags. 
        Return a JSON object: {{"email_tags": {{"email_id": ["tag1", "tag2"]}}}}
        
        Emails:
        {json.dumps(email_data, indent=2)}
        """
        try:
            response = self.model.generate_content(prompt)
            return self._extract_json(response.text)
        except:
            return {}

    def generate_tag_query(self, selected_tags, api_key=None):
        """
        Generate a Gmail search query for a group of tags.
        """
        model = self._setup_model(api_key)
        if not model: return ""
        
        prompt = f"Generate a single Gmail search query that effectively finds emails related to these topics: {selected_tags}."
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except:
            return " OR ".join(selected_tags)

    def classify_emails(self, email_summaries, api_key=None):
        model = self._setup_model(api_key)
        if not model:
            return {"error": "Gemini API key not configured"}

    def _extract_json(self, text):
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].split("```")[0].strip()
        return json.loads(text)

ai_service = AIService()
