from flask import Flask, request, json, jsonify, make_response
from api.resources.questions import Question

app = Flask(__name__)

@app.route('/api/v1/questions', methods=['POST'])
def post_a_question():
    json_data = request.data
    data = json.loads(json_data)
    data_keys = data.keys()  

    if 'user_id' not in data_keys:
        responseObject = {'message': 'Question has no user_id key'}
        return make_response(jsonify(responseObject)), 400

    if 'details' not in data_keys:
        responseObject = {'message': 'Question has no details key'}
        return make_response(jsonify(responseObject)), 400

    if data['user_id'] == 0:
        responseObject = {'message': 'Question has no specified user attached to it'}
        return make_response(jsonify(responseObject)), 400

    if data['details'] == '':
        responseObject = {'message': 'Question has no specified details'}
        return make_response(jsonify(responseObject)), 400

    """if data in question.question_tb:
        responseObject = {'message': 'Question has no specified details'}
        return make_response(jsonify(responseObject)), 400"""

    responseObject = {'message': 'Question was successfully created'}
    return make_response(jsonify(responseObject)), 201

if __name__ == '__main__':
    app.run(debug=True)