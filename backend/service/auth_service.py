from dao.user_dao import UserDao
from exception.login_error import LoginError
from util.helpers import validate_password


class AuthService:

    def __init__(self):
        self.user_dao = UserDao()

    def login(self, email, password):
        user = self.user_dao.get_user(email)
        if not user:
            raise LoginError('Invalid username and/ password combination.')
        if not validate_password(password, user.password):
            raise LoginError('Invalid username and/ password combination.')
        return user.to_dict()
