from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from app.controllers import IngredientController
from app.services.base_service import BaseService

ingredient = Blueprint('ingredient', __name__)

@ingredient.route('/', methods=POST)
def create_ingredient():
    return BaseService().create(request, IngredientController)

@ingredient.route('/', methods=PUT)
def update_ingredient():
    return BaseService().update(request, IngredientController)

@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return BaseService().get_by_id(_id, IngredientController)

@ingredient.route('/', methods=GET)
def get_ingredients():
    return BaseService().get_all(IngredientController)

