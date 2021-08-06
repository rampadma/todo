import traceback

from chalice import Blueprint, Response

from chalicelib import handle_error
from chalicelib.service.user_service import UserService

user = Blueprint(__name__)


@user.route('/user', methods=['POST'])
def add():
    try:
        return UserService().add_user(user.current_request.json_body)
    except Exception as e:
        traceback.print_exc()
        return handle_error(e)


@user.route('/user/{user_id}', methods=['PUT'])
def modify():
    try:
        return UserService().update_user(user.current_request.json_body)
    except Exception as e:
        traceback.print_exc()
        raise handle_error(e)


@user.route('/user/{user_id}', methods=['DELETE'])
def delete(user_id: str):
    try:
        UserService().delete_user(user_id)
        return Response(body={"status": "success", "debugMessage": "Successfully deleted user {}".format(user_id)})
    except Exception as e:
        traceback.print_exc()
        return handle_error(e)


@user.route('/user/{user_id}', methods=['GET'])
def get(user_id: str):
    try:
        user = UserService().get_user(user_id)
        return {
            'id': user.get('id'),
            'firstName': user.get('first_name'),
            'lastName': user.get('last_name'),
            'initials': user.get('abbr'),
            'timeZone': user.get('time_zone')
        }
    except Exception as e:
        traceback.print_exc()
        return handle_error(e)


@user.route('/users', methods=['GET'])
def get_all():
    return UserService().get_all_users()
