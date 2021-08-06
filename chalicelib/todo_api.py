import json
import traceback
from datetime import datetime

import pytz
from chalice import Blueprint

from chalicelib import handle_error
from chalicelib.service.todo_service import TodoService
from chalicelib.service.user_service import UserService

todo = Blueprint(__name__)


@todo.route('/todo', methods=['POST'])
def add():
    try:
        request_body = todo.current_request.json_body
        return TodoService().add_todo(request_body)
    except Exception as e:
        traceback.print_exc()
        return handle_error(e)


@todo.route('/todo', methods=['PUT'])
def update():
    try:
        return TodoService().update_todo(todo_data=todo.current_request.json_body,
                                         query_params=todo.current_request.query_params)
    except Exception as e:
        traceback.print_exc()
        return handle_error(e)


@todo.route('/todo/{todo_id}/{status}', methods=['PUT'])
def update_status(todo_id: str, status: str):
    try:
        TodoService().update_status(todo_id=todo_id, status=status)
        return TodoService().get_todo(todo_id)
    except Exception as e:
        traceback.print_exc()
        return handle_error(e)


@todo.route('/todo/archive/{todo_id}', methods=['PUT'])
def archive(todo_id: str):
    try:
        TodoService().archive_todo(todo_id=todo_id)
        return TodoService().get_todo(todo_id)
    except Exception as e:
        traceback.print_exc()
        return handle_error(e)


@todo.route('/todo/{todo_id}', methods=['DELETE'])
def delete(todo_id: str):
    TodoService.delete_todo(todo_id=todo_id, query_params=todo.current_request.query_params)


@todo.route('/todo/{todo_id}', methods=['GET'])
def get(todo_id: str):
    return TodoService().get_todo(todo_id=todo_id, query_params=todo.current_request.query_params)


@todo.route('/todos/{user_id}', methods=['GET'])
def get_all():
    # TODO Do paginated fetch from dynamodb
    pass


@todo.route('/todos/search/{user_id}', methods=['GET'])
def search_by_title(user_id: str):
    return TodoService().query_by_title(user_id, todo.current_request.query_params.get('title'))


@todo.route('/todos/{user_id}/{status}', methods=['GET'])
def get_by_status(user_id: str, status: str):
    # TODO Do paginated fetch from dynamodb
    return TodoService().query_by_status(user_id, status)


@todo.route('/todos/due/{user_id}', methods=['GET'])
def get_past_due(user_id: str):

    date_time: datetime = datetime.now()
    user = UserService().get_user(user_id)
    local_date_time = int(pytz.timezone(user['time_zone']).localize(date_time).timestamp()) * 1000
    return TodoService().query_past_due(user_id, local_date_time)
