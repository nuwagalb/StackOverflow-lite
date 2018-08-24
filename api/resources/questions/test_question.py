import unittest
from api.resources.questions.question import Question

class QuestionTestCase(unittest.TestCase):
    def setUp(self):
        self.question = Question(1, "What is AJAX")

    #def tearDown(self):
        #del self.question

    def test_save_method_assigns_id_to_question_and_appends_it_to_our_list(self):
        """Tests question is saved with a valid id and returns True on completion"""
        self.question = Question(3, 'Where were we')
        result = self.question.save()
        self.assertTrue(result)
    def test_find_method_returns_message_on_none_existent_record(self):
        """Tests find method returns a not found message on none existent question"""
        self.question.save()
        self.assertEqual(self.question.find(2), "Question does not exist")

    def test_find_method_returns_question_if_it_exists(self):
        self.question.save()
        self.assertIn(
                      {'id': 1, 'user_id': 1, 'question_details': 'What is AJAX'}, 
                      self.question.all_questions
        )