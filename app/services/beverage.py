
from flask import Blueprint, jsonify, request

from app.common.http_methods import GET, POST, PUT
from app.controllers.beverage import BeverageController
from app.services.base_service import BaseService


beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
def create_beverage():
    return BaseService().create(request, BeverageController)



@beverage.route('/', methods=PUT)
def update_beverage():
    return BaseService().update(request, BeverageController)



@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return BaseService().get_by_id(_id, BeverageController)



@beverage.route('/', methods=GET)
def get_beverages():
    return BaseService().get_all(BeverageController)
