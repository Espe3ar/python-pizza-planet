from typing import List
from .base_manager import BaseManager
from app.repositories.models.order import Order
from app.repositories.models.order_ingredient import OrderIngredient
from app.repositories.models.order_beverage import OrderBeverage
from app.repositories.serializers.order_serializer import OrderSerializer
from app.repositories.models.ingredient import Ingredient
from app.repositories.models.beverage import Beverage

class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        try:
            order_ingredients = [
                OrderIngredient(
                    order_id=new_order._id,
                    ingredient_id=ingredient._id,
                    ingredient_price=ingredient.price,
                ) for ingredient in ingredients
            ]
            order_beverages = [
                OrderBeverage(
                    order_id=new_order._id,
                    beverage_id=beverage._id,
                    beverage_price=beverage.price,
                ) for beverage in beverages
            ]
            cls.session.add_all(order_ingredients + order_beverages)
            cls.session.commit()
            return cls.serializer().dump(new_order)
        except Exception as e:
            cls.session.rollback()
            raise e

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not supported for {cls.__name__}')