class User:
    """Class that handles all the actions that can be performed
       on a User such as: creating a new user, viewing details 
       of a user, updating a user's details and deleting a user
    """

    user_tb = []

    def __init__(self):
        """Initializes the User class"""
        self.id = 0
        self.username = ''
        self.email = ''
        self.password = ''