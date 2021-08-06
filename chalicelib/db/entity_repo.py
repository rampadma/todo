from abc import ABC


class UserRepo(ABC):

    table_name = 'user'

    def fetch_user(self, user_id: str):
        pass

    def add_user(self, user):
        pass

    def delete_user(self, user_id):
        pass

    def update_user(self, user):
        pass


class TodoRepo(ABC):

    table_name = 'todo'

    def fetch_todo(self, todo_id: str):
        pass

    def add_todo(self, todo):
        pass

    def delete_todo(self, todo_id: str):
        pass

    def update_status(self, todo_id: str, status: str):
        pass

    def archive_todo(self, todo_id: str):
        pass

    def update_due_date(self, todo_id: str, due_date: int):
        pass

    def query_past_due(self, user_id: str, due_date: int):
        pass

    def query_by_title(self, user_id: str, title: str):
        pass

    def query_by_status(self, user_id: str, status: str):
        pass
