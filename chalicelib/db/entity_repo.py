from abc import ABC


class UserRepo(ABC):

    def fetch_user(self, user_id: str):
        pass

    def add_user(self, user):
        pass

    def delete_user(self, user_id):
        pass

    def update_user(self, user):
        pass


class TodoRepo(ABC):

    def fetch_todo(self, todo_id: int):
        pass

    def add_todo(self, todo):
        pass

    def delete_todo(self, todo_id: int):
        pass

    def update_todo(self, todo):
        pass
