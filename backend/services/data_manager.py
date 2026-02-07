import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
TAGS_FILE = os.path.join(DATA_DIR, 'tags.json')
EMAILS_FILE = os.path.join(DATA_DIR, 'emails.json')

class DataManager:
    def __init__(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        
        if not os.path.exists(TAGS_FILE):
            with open(TAGS_FILE, 'w') as f:
                json.dump([], f)
        
        if not os.path.exists(EMAILS_FILE):
            with open(EMAILS_FILE, 'w') as f:
                json.dump([], f)

    def get_tags(self):
        with open(TAGS_FILE, 'r') as f:
            return json.load(f)

    def save_tag(self, tag_name):
        tags = self.get_tags()
        if tag_name not in tags:
            tags.append(tag_name)
            with open(TAGS_FILE, 'w') as f:
                json.dump(tags, f)
        return tags

    def delete_tag(self, tag_name):
        tags = self.get_tags()
        if tag_name in tags:
            tags.remove(tag_name)
            with open(TAGS_FILE, 'w') as f:
                json.dump(tags, f)
        return tags

    def save_emails(self, emails):
        """
        emails: list of dicts. We update or append based on 'id'.
        """
        existing = self.get_emails()
        existing_ids = {e['id']: i for i, e in enumerate(existing)}
        
        for email in emails:
            if email['id'] in existing_ids:
                existing[existing_ids[email['id']]] = email
            else:
                existing.append(email)
        
        with open(EMAILS_FILE, 'w') as f:
            json.dump(existing, f, indent=2)

    def get_emails(self):
        with open(EMAILS_FILE, 'r') as f:
            return json.load(f)

    def clear_emails(self):
        with open(EMAILS_FILE, 'w') as f:
            json.dump([], f)

data_manager = DataManager()
