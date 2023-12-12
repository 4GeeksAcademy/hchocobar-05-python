from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")  # Define ruta y método
def hello_world():
    # comando de python
    # return por default si es string, devuelve HTML
    # return por default si es dict, list entonces devuelve un json.
    # response_body = {'mensaje': 'hello world!',
    #                 'results': 'Metdo GET del /'}
    return "<h1>Hello, World!</h1>"
    # return response_body


@app.route('/todos', methods=['GET', 'POST'])
def handle_todos():
    if request.method == 'GET':
        response_body = todos
        return response_body
    if request.method == 'POST':  # preguntar si el usuario tiene permisos para realizar un POST
        request_body = request.json
        # data = request.json
        # print("******", request_body)
        todos.append(request_body)
        response_body = todos
        # response_body['results'] = todos
        # response_body['message'] = 'Tarea agregada'
        return response_body


""" 
@app.route('/todos', methods=['POST'])
def add_new_todo():
"""


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print('--------------', position)
    del todos[position]
    response_body = todos
    return response_body



some_data = {"name": "Bobby", "lastname": "Rixer"}
todos = [{ "label": "My first task", "done": False },
         { "label": "My second task", "done": False }]


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
