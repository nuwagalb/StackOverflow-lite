class Answer:
    """Class that handles all the actions that can be performed
       on an Answer such as: creating a new answer, viewing 
       details of an answer, updating an answer's details and 
       deleting an answer
    """
    answer_tb = []
    
    def __init__(self):
        """Initialize Answer class"""
        self.id = 0
        self.question_id = 0
        self.user_id = 0
        self.details = ''