from chalice import Chalice

from chalicelib.todo_api import todo
from chalicelib.user_api import user

app = Chalice(app_name='todo')
app.register_blueprint(todo)
app.register_blueprint(user)


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/p/health')
def health():
    return {'Status': 'Running'}
