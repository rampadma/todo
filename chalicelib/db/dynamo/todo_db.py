from chalicelib.db.dynamo import dynamodb_support
from chalicelib.db.entity_repo import TodoRepo


class TodoDynamoDB(TodoRepo):
    def fetch_todo(self, todo_id: int):
        super().fetch_todo(todo_id)

    def add_todo(self, todo):
        return dynamodb_support.put_item(todo)

    def delete_todo(self, todo_id: int):
        super().delete_todo(todo_id)

    def update_todo(self, todo):
        super().update_todo(todo)