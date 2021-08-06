from chalicelib.db.dynamo import dynamodb_support
from chalicelib.db.entity_repo import UserRepo


class UserDynamoDB(UserRepo):

    table_name = 'user'

    def fetch_user(self, user_id: str):
        return dynamodb_support.get_by_id(self.table_name, user_id)

    def add_user(self, user):
        return dynamodb_support.put_item(self.table_name, item=user)

    def delete_user(self, user_id):
        return dynamodb_support.delete_item(self.table_name, key=user_id)

    def get_all_user(self):
        return dynamodb_support.sca

    def update_user(self, user):
        pass
