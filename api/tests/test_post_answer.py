from flask import jsonify, json, make_response
from app import app
import unittest
from api.resources.questions.question import Question

class PostAnswerApiTestCase(unittest.TestCase):
    def setUp(self):
        """Sets up a new wsgi instance for the application"""
        self.app = app.test_client()

    def test_for_undefined_question_id(self):
        """Tests for missing user_id key"""
        response = self.app.post('/api/v1/<int:questionId>/answers', 
                                content_type="application/json", 
                                data=json.dumps({'answer_details': 'It is okay'}))
        self.assertEqual(response.status_code, 404)

    def test_for_undefined_question_details_key(self):
        """Tests for missing answer_details"""
        response = self.app.post('/api/v1/<int:questionId>/answers', 
                                content_type="application/json", 
                                data=json.dumps({
                                    'user_id': 1
                                }))
        self.assertEqual(response.status_code, 404)

    def test_for_successfull_creation_of_resource(self):
        response = self.app.post('/api/v1/1/answers', 
                                 content_type="application/json",
                                 data=json.dumps({
                                     'user_id': 1, 
                                     "answer_details": "It is okay"
                                 }))
        for question in Question.all_questions:
            if question.get('id') == 1:
                self.assertEqual(response.status_code, 201)