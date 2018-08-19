import unittest
from resources.users import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        """Sets up a new instance of the User class"""
        self.user = User()
    
    def test_user_class_variable_is_of_type_list(self):
        """Test that User class has a class variable of type list"""
        self.assertTrue(isinstance(self.user.user_tb, list))

    def test_proper_initialization_of_user_class(self):
        """Tests that User class has been initialized correctly"""
        self.assertEqual(self.user.id, 0)
        self.assertEqual(self.user.username, '')
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')