import unittest
from api.resources.question import Question

class QuestionTestCase(unittest.TestCase):
    def setUp(self):
        """Sets up a new instance of the Question class"""
        self.question = Question()

    def test_question_class_variable_is_of_type_list(self):
        """Test that Question class has a class variable of type list"""
        self.assertTrue(isinstance(self.question.question_tb, list))

    def test_for_proper_initialization_of_the_answer_class(self):
        """Tests for proper initialization of the Question class"""
        self.assertEqual(self.question.id, 0)
        self.assertEqual(self.question.user_id, 0)
        self.assertEqual(self.question.question_details, '')