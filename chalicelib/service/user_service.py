import uuid
from abc import ABC

from chalicelib.db.dynamo.user_db import UserDynamoDB


class UserService(ABC):

    def add_user(self, user, query_params=None):
        print("Adding user {}", user['firstName'])
        user_id = uuid.uuid4().hex
        UserDynamoDB().add_user({
            'id': user_id,
            'first_name': user.get('firstName'),
            'last_name': user.get('lastName'),
            'abbr': user.get('initials'),
            'time_zone': user.get('timeZone'),
            'active': 1
        })
        user['id'] = user_id
        return user

    def get_user(self, user_id: str):
        return UserDynamoDB().fetch_user(user_id)

    def update_user(self, user, query_params=None):
        return UserDynamoDB().update_user(user)

    def delete_user(self, user_id):
        return UserDynamoDB().delete_user(user_id)

    def get_all_users(self):
        return UserDynamoDB().get_all_user()
