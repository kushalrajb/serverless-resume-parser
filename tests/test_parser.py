import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lambda')))
# Imports directly from parser.py now
from parser import extract_email

class TestResumeParser(unittest.TestCase):
    
    def test_extract_email_standard(self):
        text = "Hello, my name is John Doe. My email is john.doe@example.com."
        self.assertEqual(extract_email(text), "john.doe@example.com")
        
    def test_no_email_found(self):
        text = "No contact details provided on this document."
        self.assertEqual(extract_email(text), "Email not found")

if __name__ == '__main__':
    unittest.main()
