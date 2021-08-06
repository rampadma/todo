from chalicelib.db.dynamo import dynamodb_support
from chalicelib.db.entity_repo import TodoRepo


class TodoDynamoDB(TodoRepo):
    def fetch_todo(self, todo_id: str):
        return dynamodb_support.get_by_id(self.table_name, key=todo_id)

    def add_todo(self, todo):
        return dynamodb_support.put_item(self.table_name, item=todo)

    def update_status(self, todo_id: str, status: str):
        return dynamodb_support.update_item(self.table_name, key={'id': todo_id},
                                            expression='set #s=:r',
                                            attribute_names={'#s': 'status'},
                                            attribute_values={
                                                ':r': status
                                            })

    def archive_todo(self, todo_id: str):
        return dynamodb_support.update_item(self.table_name, key={'id': todo_id},
                                            expression='set #a=:r',
                                            attribute_names={'#a': 'archived'},
                                            attribute_values={
                                                ':r': True
                                            })

    def delete_todo(self, todo_id: str):
        return dynamodb_support.update_item(self.table_name, key={'id': todo_id},
                                            expression='set #a=:r',
                                            attribute_names={'#a': 'deleted'},
                                            attribute_values={
                                                ':r': True
                                            })

    def update_due_date(self, todo_id: str, due_date: int):
        return dynamodb_support.update_item(self.table_name, key={'id': todo_id},
                                            expression='set #d=:r',
                                            attribute_names={'#d': 'due_date'},
                                            attribute_values={
                                                ':r': due_date
                                            })

    def query_past_due(self, user_id: str, due_date: int):
        query = {
            "TableName": self.table_name,
            "IndexName": "user_due_date_index_1",
            "KeyConditionExpression": "#u = :u And #d > :d",
            "ExpressionAttributeNames": {"#u": "user", "#d": "due_date"},
            "ExpressionAttributeValues": {":u": user_id, ":d": due_date}
        }

        return dynamodb_support.query(self.table_name, query)

    def query_by_title(self, user_id: str, title: str):
        query = {
            "TableName": self.table_name,
            "IndexName": "user_title_index_1",
            "KeyConditionExpression": "#u = :u And begins_with(#t, :t)",
            "ExpressionAttributeNames": {"#u": "user", "#t": "title"},
            "ExpressionAttributeValues": {":u": user_id, ":t": title}
        }
        return dynamodb_support.query(self.table_name, query)

    def query_by_status(self, user_id: str, status: str):
        query = {
            "TableName": self.table_name,
            "IndexName": "user_status_index_1",
            "KeyConditionExpression": "#u = :u And #s = :s",
            "ExpressionAttributeNames": {"#u": "user", "#s": "title"},
            "ExpressionAttributeValues": {":u": user_id, ":s": status}
        }
        return dynamodb_support.query(self.table_name, query)
