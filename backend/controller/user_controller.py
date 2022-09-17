from flask import Blueprint, request
from exception.invalid_parameter_value import InvalidParameter
from service.user_service import UserService
from model.user import User
from exception.no_user_error import UserNotFound

uc = Blueprint("user_controller", __name__)
user_service = UserService()


@uc.route('/users', methods=['POST'])
def signup():
    r_body = request.get_json()

    try:
        email = r_body.get('email', None)
        first_name = r_body.get('first_name', None)
        last_name = r_body.get('last_name', None)
        password = r_body.get('password', None)
        phone = r_body.get('phone', None)
        role_name = "user"
        added_user = user_service.add_user(User(None, first_name, last_name, email, password, phone, role_name,
                                                None, None))
        return added_user, 200
    except InvalidParameter as e:
        return {
                   "message": str(e)
               }, 400


@uc.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):

    r_body = request.get_json()

    try:
        db_user = user_service.get_user(user_id)
        email = r_body.get('email', None)
        first_name = r_body.get('first_name', None)
        last_name = r_body.get('last_name', None)
        password = r_body.get('password', None)
        phone = r_body.get('phone', None)
        added_user = user_service.update_user(db_user, email, first_name, last_name, password, phone)

        return added_user, 200
    except InvalidParameter as e:
        return {
                    "message": str(e)
               }, 400
    except UserNotFound as e:
        return {
                   "message": str(e)
               }, 404
