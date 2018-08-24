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
        self.question_details = question

    def save(self):
        question_with_id = {}
        if not Question.all_questions:
             id = 1
        else:
            id = self.all_questions[-1].get('id') + 1
        question_with_id['id'] = id
        question_with_id['user_id'] = self.user_id
        question_with_id['question_details'] = self.question_details
        self.all_questions.append(question_with_id)
        return True

    def find(self, question_id):
        self.search_question_id = question_id
        if self.search_question_id:
            for question in self.all_questions:
                if question.get('id') == self.search_question_id:
                    return question
                else:
                    return 'Question does not exist'
                    


