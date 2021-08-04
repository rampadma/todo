import json

from chalice import Blueprint

from chalicelib.service.todo_service import TodoService

todo = Blueprint(__name__)


@todo.route('/todo', methods=['POST'])
def add():
    request_body = todo.current_request.json_body
    TodoService().add_todo(request_body)


@todo.route('/todo/{todo_id}', methods=['PUT'])
def modify(todo_id: str):
    pass


@todo.route('/todo/{todo_id}', methods=['DELETE'])
def delete(todo_id: str):
    pass


@todo.route('/todo/{todo_id}', methods=['GET'])
def get(todo_id: str):
    pass


@todo.route('/todos', methods=['GET'])
def get_all():
    #TODO Do paginated fetch from dynamodb
    pass
