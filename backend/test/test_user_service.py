import pytest

from model.user import User
from controller.user_controller import user_service
from exception.no_user_error import UserNotFound
from exception.invalid_parameter_value import InvalidParameter


def test_get_user_by_id(mocker):
    def mock_get_user_by_id(self, user_id):
        return User(1, 'John', 'Doe', 'jd80@a.ca',
                    '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2'.encode(),
                    '555-555-5000', 'user', None, None)

    mocker.patch('dao.user_dao.UserDao.get_user_by_id', mock_get_user_by_id)

    # Actual
    actual = user_service.get_user(1).to_dict()
    expected = {
        "user_id": 1,
        "first_name": 'John',
        "last_name": 'Doe',
        "email": 'jd80@a.ca',
        "phone": '555-555-5000',
        "role_name": 'user',
        "description": None,
        "photo": None
    }

    # Assert
    assert actual == expected


def test_get_user_by_invalid_id(mocker):
    # Arrange

    def mock_get_user_by_id(self, user_id):
        return None

    mocker.patch('dao.user_dao.UserDao.get_user_by_id', mock_get_user_by_id)

    # Act and  # Assert
    with pytest.raises(UserNotFound):
        user_service.get_user(1)


def test_add_user(mocker):
    # when user does not exist
    def mock_get_user(self, email):
        return None

    def mock_add_user(self, user):
        return User(1, 'John', 'Doe', 'jd80@a.ca',
                    'encoded password',
                    '555-555-5000', 'user', None, None)

    mocker.patch('dao.user_dao.UserDao.add_user', mock_add_user)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user)

    # Actual
    actual = user_service.add_user(User(1, 'John', 'Doe', 'jd80@a.ca',
                                        'Zxcvbnm@99$',
                                        '555-555-5000', 'user', None, None))
    expected = {
        "user_id": 1,
        "first_name": 'John',
        "last_name": 'Doe',
        "email": 'jd80@a.ca',
        "phone": '555-555-5000',
        "role_name": 'user',
        "description": None,
        "photo": None
    }

    # Assert
    assert actual == expected


def test_add_user_existing_email(mocker):
    # when user does not exist
    def mock_get_user(self, email):
        return User(1, 'John', 'Doe', 'jd80@a.ca',
                    'encoded password',
                    '555-555-5000', 'user', None, None)

    def mock_add_user(self, user):
        return User(1, 'John', 'Doe', 'jd80@a.ca',
                    'encoded password',
                    '555-555-5000', 'user', None, None)

    mocker.patch('dao.user_dao.UserDao.add_user', mock_add_user)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user)

    with pytest.raises(InvalidParameter):
        user_service.add_user(User(None, 'Jane', 'Doe', 'jd80@a.ca',
                    '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2'.encode(),
                    '555-555-5000', 'user', None, None))


def test_add_user_DB_error(mocker):
    # when user does not exist
    def mock_get_user(self, email):
        return None

    def mock_add_user(self, user):
        return None

    mocker.patch('dao.user_dao.UserDao.add_user', mock_add_user)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user)

    with pytest.raises(InvalidParameter):
        user_service.add_user(User(None, 'Jane', 'Doe', 'jd80@a.ca',
                    '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2'.encode(),
                    '555-555-5000', 'user', None, None))


def test_update_user_positive(mocker):

    def mock_get_user(self, email):
        # User this email does not exist
        return None

    def mock_update_user(self, user, email, first_name, last_name, password, phone):
        return User(1, 'Jane', 'Doe', 'jd80@a.ca',
                    '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2'.encode(),
                    '555-555-5000', 'user', None, None)

    mocker.patch('dao.user_dao.UserDao.update_user', mock_update_user)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user)

    # Actual
    actual = user_service.update_user(
        User(1, 'John', 'Doe', 'jd80@a.ca', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2'.encode(), '555-555-5000', 'user', None, None),
        'cat@tech.co', 'Jane', None, None, None)

    expected = {
        "user_id": 1,
        "first_name": 'Jane',
        "last_name": 'Doe',
        "email": 'jd80@a.ca',
        "phone": '555-555-5000',
        "role_name": 'user',
        "description": None,
        "photo": None
    }

    # Assert
    assert actual == expected



def test_update_user_negative(mocker):

    def mock_get_user(self, email):
        # User this email does not exist
        return User(1, 'Cat', 'Toe', 'cat@tech.co',
                    '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2'.encode(),
                    '555-255-5000', 'admin', None, None)

    def mock_update_user(self, user, email, first_name, last_name, password, phone):
        return User(1, 'Jane', 'Doe', 'jd80@a.ca',
                    '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2'.encode(),
                    '555-555-5000', 'user', None, None)

    mocker.patch('dao.user_dao.UserDao.update_user', mock_update_user)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user)

    # Act and  # Assert
    with pytest.raises(InvalidParameter):
        user_service.update_user(
        User(1, 'John', 'Doe', 'jd80@a.ca', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2'.encode(), '555-555-5000', 'user', None, None),
        'cat@tech.co', 'Jane', None, None, None)


def test_update_user_negative_no_phone_names_password(mocker):

    def mock_get_user(self, email):
        # User this email does not exist
        return None

    def mock_update_user(self, user, email, first_name, last_name, password, phone):
        return User(1, 'John', 'Doe', 'jd80@a.ca',
                    '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2'.encode(),
                    '555-555-5000', 'user', None, None)

    mocker.patch('dao.user_dao.UserDao.update_user', mock_update_user)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user)

    # Act and  # Assert
    with pytest.raises(InvalidParameter):
        user_service.update_user(
        User(1, 'John', 'Doe', 'jd80@a.ca', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2'.encode(), '555-555-5000', 'user', None, None),
        'cat@tech.co', None, None, None, None)
