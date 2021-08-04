import datetime
import json
import uuid
from abc import ABC

import pytz

from chalicelib.db.dynamo.todo_db import TodoDynamoDB
from chalicelib.db.dynamo.user_db import UserDynamoDB


class TodoService(ABC):

    def add_todo(self, todo_data: json, query_params=None):

        user_id = todo_data.get('user_id')
        due_date = todo_data.get('dueDate')
        user = UserDynamoDB().fetch_user(user_id=user_id)

        local_date_time: datetime = pytz.timezone(user['time_zone'])

        TodoDynamoDB().add_todo({
            'id': uuid.uuid4().hex,
            'title': todo_data.get('title'),
            'due_date': todo_data.get('dueDate'),
            'completed': False,
            'archived': False,
            'user': user_id
        })
