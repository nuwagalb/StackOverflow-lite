import unittest
from api.resources.questions.question import Question

class QuestionTestCase(unittest.TestCase):
    def setUp(self):
        self.question = Question(1, "What is Continous Integration")

    #def tearDown(self):
        #del self.question

    def test_save_method_assigns_id_to_question_and_appends_it_to_our_list(self):
        """Tests for successful insertion of a question into the db"""
        self.question = Question(3, 'Where were we')
        self.assertTrue(self.question.save())