import pytest

from controller.auth_controller import auth_service
from exception.login_error import LoginError
from model.user import User


def test_login_valid_username_valid_password(mocker):
    #  Arrange
    def mock_get_user(self, email):
        return User(1, 'John', 'Doe', 'jd80@a.ca',
                    '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2'.encode(),
                    '555-555-5000', 'user', None, None)

    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user)

    # Act
    actual = auth_service.login('jd80@a.ca', 'password')

    # Assert
    assert actual == {'user_id': 1, 'first_name': 'John', 'last_name': 'Doe', 'email': 'jd80@a.ca',
                      'phone': '555-555-5000', 'role_name': 'user', 'description': None, 'photo': None}


def test_login_valid_username_invalid_password(mocker):
    #  Arrange
    def mock_get_user(self, email):
        return User(1, 'John', 'Doe', 'jd80@a.ca',
                    '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2'.encode(),
                    '555-555-5000', 'user', None, None)

    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user)

    # Act and  # Assert
    with pytest.raises(LoginError):
        auth_service.login('jd80@a.ca', 'password1')

def test_login_invalid_username(mocker):
    #  Arrange
    def mock_get_user(self, email):
        return None

    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user)

    # Act and  # Assert
    with pytest.raises(LoginError):
        auth_service.login('j', 'password')



