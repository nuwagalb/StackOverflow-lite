from flask import jsonify, json, make_response
from app import app
import unittest
#from api.resources.questions import Question
class AppTestCase(unittest.TestCase):
    def setUp(self):
        """Sets up a new wsgi instance for the application"""
        self.app = app.test_client()
        #self.question = Question()

    def test_for_undefined_user_id(self):
        """Tests for missing user_id key"""
        response = self.app.post('/api/v1/questions', 
                                content_type="application/json", 
                                data=json.dumps({'details': 'What is AJAX?'}))
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message'], 'Question has no user_id key')

    def test_for_undefined_details_key(self):
        """Tests for missing details key"""
        response = self.app.post('/api/v1/questions', 
                                content_type="application/json", 
                                data=json.dumps({'user_id': 1}))
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message'], 'Question has no details key')

    def test_for_empty_user_id(self):
        """Tests for empty user id values"""
        response = self.app.post('/api/v1/questions', 
                                content_type="application/json", 
                                data=json.dumps({'user_id': 0, 'details': 'What is AJAX?'}))
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message'], 'Question has no specified user attached to it')

    def test_for_empty_details(self):
        """Tests for empty details value"""
        response = self.app.post('/api/v1/questions', 
                                content_type="application/json", 
                                data=json.dumps({'user_id': 1, 'details': ''}))
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message'], 'Question has no specified details')

    #def test_for_already_existing_question(self):
        """self.question.question_tb = [{"id":1, "user_id":1, "details":"What is AJAX?"}]
        response = self.app.post('api/v1/questions', 
                                 content_type="application/json",
                                 data=json.dumps({"id":1, 'user_id': 1, "details": "What is AJAX"}))
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message'], 'Question already exists')"""

    def test_for_successfull_creation_of_resource(self):
        response = self.app.post('api/v1/questions', 
                                 content_type="application/json",
                                 data=json.dumps({'user_id': 1, "details": "What is AJAX"}))
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data['message'], 'Question was successfully created')

        




                            