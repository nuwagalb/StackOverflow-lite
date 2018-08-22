import unittest
from api.resources.base_function import BaseFunction

class BaseFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.base_function = BaseFunction([{'user_id': 1, 'question_details': 'What is AJAX'}])

    def test_for_proper_initialization_of_base_class(self):
        self.assertIsInstance(self.base_function.record_details, list)

    def test_save_method(self):
        self.assertEqual(self.base_function.save(), 
                         [{'id': 1, 'user_id': 1, 'question_details': 'What is AJAX'}])
