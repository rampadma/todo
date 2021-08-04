from chalice import Blueprint

user = Blueprint(__name__)


@user.route('/users', methods=['POST'])
def add():
    pass


@user.route('/users/{user_id}', methods=['PUT'])
def modify(user_id: str):

    pass


@user.route('/users/{user_id}', methods=['DELETE'])
def delete(user_id: str):
    pass


@user.route('/users/{user_id}', methods=['GET'])
def get(user_id: str):
    pass


@user.route('/users', methods=['GET'])
def get_all():
    #TODO Do paginated fetch from dynamodb
    pass
