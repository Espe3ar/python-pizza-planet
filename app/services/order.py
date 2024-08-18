from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from app.services.base_service import BaseService

from ..controllers import OrderController

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    return BaseService().create(request, OrderController)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return BaseService().get_by_id(_id, OrderController)


@order.route('/', methods=GET)
def get_orders():
    return BaseService().get_all(OrderController)
