import unittest
from resources.answers import Answer

class AnswerTestCase(unittest.TestCase):
    def setUp(self):
        """Sets up a new instance of the Answer class"""
        self.answer = Answer()

    def test_answer_class_variable_is_of_type_list(self):
        """Test that Answer class has a class variable of type list"""
        self.assertTrue(isinstance(self.answer.answer_tb, list))

    def test_for_proper_initialization_of_the_answer_class(self):
        """Tests for proper initialization of the Answer class"""
        self.assertEqual(self.answer.id, 0)
        self.assertEqual(self.answer.question_id, 0)
        self.assertEqual(self.answer.user_id, 0)
        self.assertEqual(self.answer.details, '')