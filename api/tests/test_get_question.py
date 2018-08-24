from flask import jsonify, json, abort
from app import app
import unittest
from api.resources.questions.question import Question

class GetQuestionApiTestCase(unittest.TestCase):
    def setUp(self):
        """Sets up a new wsgi instance for the application"""
        self.app = app.test_client()

    def test_endpoint_returns_not_found_status_code_on_unavailable_resource(self):
        """Tests Not Found status code for unavailable resource"""
        response = self.app.get('/api/v1/questions/<questionId>', 
                                 content_type="application/json",
                                 data=json.dumps(1))
        search_id = response.data
        if Question.all_questions:
            for question in Question.all_questions:
                if question.get('id') != search_id:
                     self.assertEqual(response.status_code, 404)

    def test_endpoint_returns_success_status_code_on_available_resource(self):
        """Tests Ok status code for available resource"""
        response = self.app.get('/api/v1/questions/<questionId>', 
                                 content_type="application/json",
                                 data=json.dumps(1))
        search_id = response.data
        if Question.all_questions:
            for question in Question.all_questions:
                if question.get('id') == search_id:
                     self.assertEqual(response.status_code, 200)




    