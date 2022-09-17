import flask
from flask import request, jsonify, Blueprint, session

from exception.login_error import LoginError
from service.auth_service import AuthService

ac = Blueprint('auth_controller', __name__)
auth_service = AuthService()


@ac.route('/login', methods=['POST'])
def login():
    email = request.json.get("email")
    password = request.json.get("password")
    try:
        user_dict = auth_service.login(email, password)
        session['user_info'] = user_dict
      
        return user_dict, 200
    except LoginError as e:
        return {
                   "message": str(e)
               }, 400


@ac.route('/logout', methods=['POST', 'OPTIONS'])
def logout():

    response = jsonify({"message": "logout successful"})
    session.clear()
    return response, 200


@ac.route('/loginstatus', methods=['GET'])
def loginstatus():
    print(session.get("user_info"))
    if session.get('user_info') is not None:
        temp_dict = session.get('user_info')

        return {
            "message": "You are logged in",
            "logged_in_user": (temp_dict['first_name'] + " " + temp_dict['last_name'])
        }, 200
    else:
        return {
            "message": "You are not logged in"
        }, 400
