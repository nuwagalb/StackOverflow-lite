class Answer:
    """Class that handles all the actions that can be performed
       on an Answer such as: creating a new answer, viewing 
       details of an answer, updating an answer's details and 
       deleting an answer
    """
    all_answers = []
    
    def __init__(self, user_id, answer):
        """Initializes the Answer class"""
        self.user_id = user_id
        self.details = answer

    def save(self):
        """Returns true when question is saved in our db"""
        if not Answer.all_answers:
             id = 1
        else:
            id = self.all_answers[-1].get('id') + 1
        
        self.all_answers.append(
             {'id': id, 'user_id': self.user_id, 'details': self.details}
        )
        return True