from chalicelib.db.dynamo import dynamodb_support
from chalicelib.db.entity_repo import UserRepo


class UserDynamoDB(UserRepo):

    def fetch_user(self, user_id: str):
        dynamodb_support.get_by_id(user_id)

    def add_user(self, user):
        super().add_user(user)

    def delete_user(self, user_id):
        super().delete_user(user_id)

    def update_user(self, user):
        super().update_user(user)