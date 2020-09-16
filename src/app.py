import json

from flask import Flask, jsonify, request


app = Flask(__name__)
todos = [
    { "done": True, "label": "Dummy" }
]

@app.route('/blabla', methods=['GET'])
def hello_world():
    return "Hello, World!"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    return get_todos()

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return get_todos()

# This line should always be at the end of your app.py file.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
