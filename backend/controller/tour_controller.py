import service.tour_service
from util.db_connection import pool
from model.tour import Tour
from model.user import User
from flask import Blueprint, request
from service.tour_service import TourService
from exception.invalid_parameter_value import InvalidParameter
from exception.tour_error import TourError

tc = Blueprint("tour_controller", __name__)
tour_service = TourService()


@tc.route('/tour/add', methods=['POST'])
def add_tour():
    rbody = request.get_json()
    print(rbody)
    try:
        guide_id = rbody['guide_id']
        day = rbody['day']
        price = rbody['price']
        title = rbody['title']
        route_id = tour_service.add_poi(rbody['pois'])
        print(route_id)
        added_tour = tour_service.add_tour(Tour(None, guide_id, route_id, day, price, title, False))

        return added_tour, 200
    except InvalidParameter as e:
        return {
                   "message": str(e)
               }, 400


@tc.route('/tours', methods=['GET'])
def get_tours():
    try:
        return {
                   "tours": tour_service.view_tours()
               }, 200
    except TourError as e:
        return {
                   "messages": str(e)
               }, 400


@tc.route('/tours/<user_id>', methods=['GET'])
def get_tours_by_id(user_id):
    try:

        return {
                   "tours": tour_service.view_tours_by_id(user_id)
               }, 200
    except TourError as e:
        return {
                   "messages": str(e)
               }, 400


@tc.route('/tour', methods=['PUT'])
def update_tour():
    rbody = request.get_json()
    try:
        price = rbody.get('price', None)
        day = rbody.get('day', None)
        tour_id = rbody.get('tour_id', None)
        inactive = rbody.get('inactive', None)

        updated_tour = tour_service.update_tours(Tour(tour_id, None, None, day, price, "None", inactive))
        return updated_tour.to_dict(), 200
    except InvalidParameter as e:
        return {
                   "message": str(e)
               }, 400


@tc.route('/tour/<tour_id>', methods=["DELETE"])
def delete_tour(tour_id):
    try:
        tour = tour_service.delete_tour(tour_id)

        if (tour == True):
            return {
                       "message": "Tour Deleted"
                   }, 200
    except TourError as e:
        return {
                   "messages": str(e)
               }, 400
