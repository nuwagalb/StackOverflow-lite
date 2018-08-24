from flask import jsonify, json, make_response
from app import app
import unittest

class PostQuestionApiTestCase(unittest.TestCase):
    def setUp(self):
        """Sets up a new wsgi instance for the application"""
        self.app = app.test_client()

    def test_for_undefined_user_id(self):
        """Tests for missing user_id key"""
        response = self.app.post('/api/v1/questions', 
                                content_type="application/json", 
                                data=json.dumps({'question_details': 'What is AJAX?'}))
        self.assertEqual(response.status_code, 400)

    def test_for_undefined_question_details_key(self):
        """Tests for missing question_details key"""
        response = self.app.post('/api/v1/questions', 
                                content_type="application/json", 
                                data=json.dumps({'user_id': 1}))
        self.assertEqual(response.status_code, 400)

    def test_for_successfull_creation_of_resource(self):
        response = self.app.post('api/v1/questions', 
                                 content_type="application/json",
                                 data=json.dumps({'user_id': 1, "question_details": "What is AJAX?"}))
        self.assertEqual(response.status_code, 201)
        



