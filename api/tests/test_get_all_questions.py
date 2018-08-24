from flask import jsonify, json
from app import app
import unittest
from api.resources.questions.question import Question

class GetAllQuestionApiTestCase(unittest.TestCase):
    def setUp(self):
        """Sets up a new wsgi instance for the application"""
        self.app = app.test_client()

    def test_returns_error_message_on_empty_questions(self):
        """Test error status code is returned on empty details"""
        response = self.app.get('/api/v1/questions')
        if not Question.all_questions:
            self.assertEqual(response.status_code, 404)

    def test_returns_success_status_code_for_valid_data(self):
        """Test success code is returned for list of things"""
        response = self.app.get('/api/v1/questions')
        if Question.all_questions:
            self.assertEqual(response.status_code, 200)
        