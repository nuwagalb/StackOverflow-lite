import unittest
from api.resources.answers.answer import Answer

class AnswerTestCase(unittest.TestCase):
    def setUp(self):
        self.answer = Answer(1, "It is mainly for making sure your code doesn't break")

    #def tearDown(self):
        #del self.question

    def test_save_method_assigns_id_to_question_and_appends_it_to_our_list(self):
        """Tests for successful insertion of an answer into the db"""
        self.Answer = Answer(3, 'Where were we')
        self.assertTrue(self.answer.save())