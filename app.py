from flask import Flask, request, json, jsonify, make_response, abort
from api.resources.questions.question import Question
from api.resources.answers.answer import Answer

application = app = Flask(__name__)

@app.route('/api/v1/questions', methods=['POST'])
def post_a_question():

    json_data = request.get_json()

    if 'user_id' not in json_data:
        response_object = {'message': 'Question has no user_id key'}
        return jsonify(response_object), 400

    if 'question_details' not in json_data:
        response_object = {'message': 'Question has no question_details key'}
        return jsonify(response_object), 400

    if not json_data['question_details']:
        response_object = {'message': 'Question has no specified question_details'}
        return jsonify(response_object), 400

    #update class Question clas svariable
    question_tb = Question(json_data['user_id'], json_data['question_details'])

    #save the new question
    question_tb.save()

    #return details that were just saved
    result = Question.all_questions[-1]

    return jsonify(result), 201

@app.route('/api/v1/questions/<int:questionId>', methods=['GET'])
def get_a_question(questionId):

    question_id = questionId
    for question in Question.all_questions:
        if question.get('id') == question_id:
            return jsonify(question), 200
        
    response_object = {'message': 'Record was not found'}
    return jsonify(response_object), 404
            
@app.route('/api/v1/questions', methods=['GET'])
def get_all_question():

    if Question.all_questions:
        return jsonify(Question.all_questions), 200

@app.route('/api/v1/<int:questionId>/answers', methods=['POST'])
def post_an_answer(questionId):
    question_id = questionId
    json_data = request.get_json()

    if 'user_id' not in json_data:
        response_object = {'message': 'Answer has no user_id key'}
        return jsonify(response_object), 404

    if 'answer_details' not in json_data:
        response_object = {'message': 'Answer has no answer_details key'}
        return jsonify(response_object), 404

    if not json_data['answer_details']:
        response_object = {'message': 'Answer has no specified answer_details'}
        return jsonify(response_object), 404

    #search if question_id exists_amongst_all_our_questions, then you can post an answer
    if Question.all_questions:
        for question in Question.all_questions:
            if question.get('id') == question_id:
                answer_tb = Answer(json_data['user_id'], json_data['answer_details'])
                #save new answer
                answer_tb.save()

                #return details that were just saved
                result = Answer.all_answers[-1]
                return jsonify(result), 201
            else:
                return jsonify({'message': 'Answer could not be added'})

if __name__ == '__main__':
    app.run(debug=False)