class Question:
    """Class that handles all the actions that can be performed
       on a Question such as: creating a new question, viewing 
       details of a question, updating a questions's details 
       and deleting a question
    """
    all_questions = []

    def __init__(self, user_id, question):
        """Initializes the Question class"""
        self.user_id = user_id
        self.details = question

    def save(self):
        """returns true if question was successfully added to db"""
        if not Question.all_questions:
             id = 1
        else:
            id = self.all_questions[-1].get('id') + 1

        self.all_questions.append(
            {'id': id, 'user_id': self.user_id, 'details': self.details}
        )
        return True

