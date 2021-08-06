import json
import uuid
from abc import ABC
from datetime import datetime

import pytz
from chalice import Response

from chalicelib.db.dynamo.todo_db import TodoDynamoDB
from chalicelib.db.dynamo.user_db import UserDynamoDB


class TodoService(ABC):

    def get_todo(self, todo_id: str, query_params=None):

        todo = TodoDynamoDB().fetch_todo(todo_id)
        user = UserDynamoDB().fetch_user(todo['user'])
        local_datetime = datetime.fromtimestamp(int(todo.get('due_date')) / 1000,
                                                tz=pytz.timezone(user.get('time_zone')))
        return {
            "id": todo.get('id'),
            "title": todo.get('title'),
            'dueDate': local_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
            'status': todo.get('status'),
            'archived': todo.get('archived'),
            'deleted': todo.get('deleted'),
            'user': {
                'id': user.get('id'),
                'firstName': user.get('first_name'),
                'lastName': user.get('last_name')
            }
        }

    def add_todo(self, todo_data: json, query_params=None):

        user_id = todo_data.get('userId')
        due_date = todo_data.get('dueDate')
        user = UserDynamoDB().fetch_user(user_id=user_id)
        date_time: datetime = datetime.strptime(due_date, '%Y-%m-%dT%H:%M:%S')
        local_date_time = int(pytz.timezone(user['time_zone']).localize(date_time).timestamp()) * 1000
        todo_id = todo_data['id'] if 'id' in todo_data else uuid.uuid4().hex
        TodoDynamoDB().add_todo({
            'id': todo_id,
            'title': todo_data.get('title'),
            'due_date': local_date_time,
            'status': todo_data['status'],
            'archived': todo_data['archived'] if 'archived' in todo_data else False,
            'deleted': False,
            'user': user_id
        })
        todo_data['id'] = todo_id
        return todo_data

    def update_status(self, todo_id: str, status: str, query_params=None):
        return TodoDynamoDB().update_status(todo_id, status)

    def delete_todo(self, todo_id: str, query_params=None):
        return TodoDynamoDB().delete_todo(todo_id)

    def archive_todo(self, todo_id: str, query_params=None):
        return TodoDynamoDB().archive_todo(todo_id)

    def update_todo(self, todo_data: json, query_params=None):

        todo_ids = []
        for data in todo_data['data']:
            todo_ids.append(data['id'])
            self.add_todo(todo_data=data, query_params=query_params)
        response = {'status': 'success', 'data': []}
        for todo_id in todo_ids:
            response['data'].append(self.get_todo(todo_id=todo_id, query_params=query_params))

        return response

    def query_past_due(self, user_id: str, due_date: int):
        data = TodoDynamoDB().query_past_due(user_id, due_date)
        return Response(body={
            "status": "success",
            "data": data
        })

    def query_by_status(self, user_id: str, status: str):
        data = TodoDynamoDB().query_by_status(user_id, status)
        return Response(body={
            "status": "success",
            "data": data
        })

    def query_by_title(self, user_id: str, title: str):
        data = TodoDynamoDB().query_by_title(user_id, title)
        return Response(body={
            "status": "success",
            "data": data
        })
