from flask import Flask, jsonify, request


app = Flask(__name__)


todos = []

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

@app.route('/api/todos', methods=['POST'])
def create_todo():
    todo = request.get_json().get('todo')
    if todo:
        new_todo = {'id': len(todos) + 1, 'title': todo}
        todos.append(new_todo)
        return jsonify({'todo': new_todo}), 201
    else:
        return jsonify({'error': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(debug=True)
