import json
import unittest
from unittest.mock import MagicMock
import sys
import os

# Add parent dir to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.ai_service import AIService

class TestAIService(unittest.TestCase):
    def test_prompt_generation(self):
        # Mock the model
        service = AIService()
        service.model = MagicMock()
        
        mock_response = MagicMock()
        mock_response.text = json.dumps({
            "categories": [
                {
                    "name": "Social",
                    "emails": ["123"],
                    "reason": "From Linkedin",
                    "search_key": "from:linkedin.com",
                    "action": "delete_recommendation"
                }
            ]
        })
        service.model.generate_content.return_value = mock_response
        
        emails = [{"id": "123", "subject": "New Job", "from": "linkedin.com", "snippet": "Check this out"}]
        result = service.classify_emails(emails)
        
        self.assertIn("categories", result)
        self.assertEqual(result["categories"][0]["name"], "Social")
        self.assertEqual(result["categories"][0]["search_key"], "from:linkedin.com")

if __name__ == '__main__':
    unittest.main()
