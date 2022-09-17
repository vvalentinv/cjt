import pytest

from controller.tour_controller import tour_service
from exception.invalid_parameter_value import InvalidParameter
from model.tour import Tour


def test_add_poi(mocker):
    #  Arrange
    def mock_add_poi(self, pois):
        return 75

    mocker.patch('dao.tour_dao.TourDao.add_poi', mock_add_poi)

    # Act
    actual = tour_service.add_poi(['3', '4', '5'])

    # Assert
    assert actual == 75


def test_add_poi_less_than_2_poi(mocker):
    #  Arrange
    def mock_add_poi(self, pois):
        return 75

    mocker.patch('dao.tour_dao.TourDao.add_poi', mock_add_poi)

    # Act and  # Assert
    with pytest.raises(InvalidParameter):
        tour_service.add_poi(['3', '4'])


def test_add_poi_more_than_5_poi(mocker):
    #  Arrange
    def mock_add_poi(self, pois):
        return 75

    mocker.patch('dao.tour_dao.TourDao.add_poi', mock_add_poi)

    # Act and  # Assert
    with pytest.raises(InvalidParameter):
        tour_service.add_poi(['3', '4', '1', '2', '6', '7'])


def test_add_tour(mocker):
    #  Arrange
    def mock_add_tour(self, pois):
        return Tour(41, 5, 75, 1, 5500, 'dfdfdf', False)

    mocker.patch('dao.tour_dao.TourDao.add_tour', mock_add_tour)

    # Act
    actual = tour_service.add_tour(Tour(None, 5, 75, '1', '55', 'dfdfdf', False))

    # Assert
    assert (actual.get("guide_id") == 5 and
            actual.get("day_of_week") == 1 and
            actual.get("price_per_person_in_cents") == '$55.0' and
            actual.get("inactive") is False)


def test_view_tours(mocker):
    #  Arrange
    def mock_get_tour(self):
        return [
            [
                "Central Park--Rockefeller Center--Metropolitan Museum of Art",
                "first addition",
                "Jenny Richmond",
                1,
                2000
            ],
            [
                "Statue of Liberty--Central Park--Rockefeller Center",
                "sfaddfsas",
                "Jenny Richmond",
                1,
                23400
            ],
            [
                "Statue of Liberty--Central Park--Rockefeller Center--Metropolitan Museum of Art",
                "gate",
                "Revere Paully",
                1,
                4800
            ]
        ]

    mocker.patch('dao.tour_dao.TourDao.get_tour', mock_get_tour)

    # Act
    actual = tour_service.view_tours()

    # Assert
    assert actual == [
        [
            "Central Park--Rockefeller Center--Metropolitan Museum of Art",
            "first addition",
            "Jenny Richmond",
            1,
            2000
        ],
        [
            "Statue of Liberty--Central Park--Rockefeller Center",
            "sfaddfsas",
            "Jenny Richmond",
            1,
            23400
        ],
        [
            "Statue of Liberty--Central Park--Rockefeller Center--Metropolitan Museum of Art",
            "gate",
            "Revere Paully",
            1,
            4800
        ]
    ]


def test_view_tours_by_user_id(mocker):
    #  Arrange
    def mock_get_tours_by_id(self, user_id):
        return [
            [
                "Statue of Liberty--Central Park--Rockefeller Center",
                "adsads",
                "Jenny Richmond",
                1,
                4400,
                31
            ],
            [
                "Central Park--Rockefeller Center--Metropolitan Museum of Art",
                "sdvdv",
                "Jenny Richmond",
                3,
                4500,
                37
            ],
            [
                "Rockefeller Center--Metropolitan Museum of Art--Broadway and the Theater District",
                "dfdfdf",
                "Jenny Richmond",
                1,
                5500,
                41
            ],
            [
                "Statue of Liberty--Central Park--Rockefeller Center",
                "dsds",
                "Jenny Richmond",
                1,
                200,
                40
            ],
            [
                "Central Park--Rockefeller Center--Metropolitan Museum of Art",
                "first addition",
                "Jenny Richmond",
                1,
                2000,
                32
            ],
            [
                "Statue of Liberty--Central Park--Rockefeller Center",
                "Third Tour",
                "Jenny Richmond",
                3,
                9900,
                3
            ],
            [
                "Statue of Liberty--Central Park--Rockefeller Center",
                "dsafads",
                "Jenny Richmond",
                1,
                2300,
                33
            ],
            [
                "Statue of Liberty--Central Park--Rockefeller Center",
                "sfaddfsas",
                "Jenny Richmond",
                1,
                23400,
                29
            ]
        ]

    mocker.patch('dao.tour_dao.TourDao.get_tours_by_id', mock_get_tours_by_id)

    # Act
    actual = tour_service.view_tours_by_id(4)

    # Assert
    assert actual == [
        [
            "Statue of Liberty--Central Park--Rockefeller Center",
            "adsads",
            "Jenny Richmond",
            1,
            4400,
            31
        ],
        [
            "Central Park--Rockefeller Center--Metropolitan Museum of Art",
            "sdvdv",
            "Jenny Richmond",
            3,
            4500,
            37
        ],
        [
            "Rockefeller Center--Metropolitan Museum of Art--Broadway and the Theater District",
            "dfdfdf",
            "Jenny Richmond",
            1,
            5500,
            41
        ],
        [
            "Statue of Liberty--Central Park--Rockefeller Center",
            "dsds",
            "Jenny Richmond",
            1,
            200,
            40
        ],
        [
            "Central Park--Rockefeller Center--Metropolitan Museum of Art",
            "first addition",
            "Jenny Richmond",
            1,
            2000,
            32
        ],
        [
            "Statue of Liberty--Central Park--Rockefeller Center",
            "Third Tour",
            "Jenny Richmond",
            3,
            9900,
            3
        ],
        [
            "Statue of Liberty--Central Park--Rockefeller Center",
            "dsafads",
            "Jenny Richmond",
            1,
            2300,
            33
        ],
        [
            "Statue of Liberty--Central Park--Rockefeller Center",
            "sfaddfsas",
            "Jenny Richmond",
            1,
            23400,
            29
        ]
    ]


def test_add_tour(mocker):
    #  Arrange
    # def mock_add_poi(self, pois):
    #     return 75

    def mock_add_tour(self, pois):
        return Tour(66, 4, 75, "1", 5500, "title", False)

    mocker.patch('dao.tour_dao.TourDao.add_tour', mock_add_tour)
    # mocker.patch('dao.tour_dao.TourDao.add_poi', mock_add_poi)
    # Act
    actual = tour_service.add_tour(Tour(None, 4, 75, "1", "55", "title", False))

    # Assert
    assert (actual.get("tour_id") == 66 and
            actual.get("guide_id") == 4 and
            actual.get("day_of_week") == "1" and
            actual.get("route_id") == 75 and
            actual.get("price_per_person_in_cents") == "$55.0" and
            actual.get("tour_name") == "title" and
            actual.get("inactive") is False)


def test_add_tour(mocker):
    #  Arrange
    # def mock_add_poi(self, pois):
    #     return 75

    def mock_update_tour(self, pois):
        return Tour(66, 4, 75, "1", 5500, "title", False)

    mocker.patch('dao.tour_dao.TourDao.update_tour', mock_update_tour)
    # mocker.patch('dao.tour_dao.TourDao.add_poi', mock_add_poi)
    # Act
    actual = tour_service.update_tours(Tour(None, None, None, "1", "55", "None", False))

    # Assert
    assert actual is not None


def test_add_tour(mocker):
    #  Arrange
    # def mock_add_poi(self, pois):
    #     return 75

    def mock_add_tour(self, pois):
        return Tour(66, 4, 75, "1", 5500, "title", False)

    mocker.patch('dao.tour_dao.TourDao.add_tour', mock_add_tour)
    # mocker.patch('dao.tour_dao.TourDao.add_poi', mock_add_poi)
    # Act
    actual = tour_service.add_tour(Tour(None, 4, 75, "1", "55", "title", False))

    # Assert
    assert (actual.get("tour_id") == 66 and
            actual.get("guide_id") == 4 and
            actual.get("day_of_week") == "1" and
            actual.get("route_id") == 75 and
            actual.get("price_per_person_in_cents") == "$55.0" and
            actual.get("tour_name") == "title" and
            actual.get("inactive") is False)


def test_update_tour(mocker):
    #  Arrange
    # def mock_add_poi(self, pois):
    #     return 75

    def mock_update_tour(self, pois):
        return Tour(66, 4, 75, "1", 5500, "title", False)

    mocker.patch('dao.tour_dao.TourDao.update_tour', mock_update_tour)
    # mocker.patch('dao.tour_dao.TourDao.add_poi', mock_add_poi)
    # Act
    actual = tour_service.update_tours(Tour(None, None, None, "1", "55", "None", False))

    # Assert
    assert actual is not None

def test_delete_tour(mocker):
    #  Arrange
    def mock_delete_tour(self, tour_id):
        return True

    mocker.patch('dao.tour_dao.TourDao.delete_tour', mock_delete_tour)

    # Act
    actual = tour_service.delete_tour(66)

    # Assert
    assert actual is True
