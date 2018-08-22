class Question:
    """Class that handles all the actions that can be performed
       on a Question such as: creating a new question, viewing 
       details of a question, updating a questions's details 
       and deleting a question
    """
    question_tb = []

    def __init__(self):
        """Initializes the Question class"""
        self.id = 0
        self.user_id = 0
        self.question_details = ''