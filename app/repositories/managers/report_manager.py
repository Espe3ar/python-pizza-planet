from typing import List
from .base_manager import BaseManager
from app.repositories.models.order import Order
from app.repositories.models.order_ingredient import OrderIngredient
from app.repositories.models.order_beverage import OrderBeverage
from app.repositories.serializers.order_serializer import OrderSerializer
from app.repositories.models.ingredient import Ingredient
from app.repositories.models.beverage import Beverage
from sqlalchemy.sql import func
from sqlalchemy import Integer


class ReportManager(BaseManager):

    @classmethod
    def get_most_requested_ingredient(cls):
        result = (
            cls.session.query(
                Ingredient.name,
                func.count(OrderIngredient.ingredient_id).label("total"),
            )
            .join(OrderIngredient)
            .group_by(Ingredient.name)
            .order_by(func.count(OrderIngredient.ingredient_id).desc())
            .first()
        )
        if result:
            return {"name": result[0], "total": result[1]}
        return {"message": "No data available"}

    @classmethod
    def get_month_with_most_revenue(cls):
        MONTH_NAMES = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        }
        result = (
            cls.session.query(
                func.cast(func.strftime("%m", Order.date), Integer),
                func.strftime("%Y", Order.date),
                func.sum(Order.total_price),
            )
            .group_by(func.strftime("%m", Order.date), func.strftime("%Y", Order.date))
            .order_by(func.sum(Order.total_price).desc())
            .first()
        )
        if result:
            month, year, revenue = result
            month_name = MONTH_NAMES[month]
            return {"month": f"{month_name} {year}", "revenue": revenue}
        return {"message": "No data available"}

    @classmethod
    def get_top_customers(cls):
        results = (
            cls.session.query(
                Order.client_name,
                func.sum(Order.total_price).label("total_spent")
            )
            .group_by(Order.client_name)
            .order_by(func.sum(Order.total_price).desc())
            .limit(3)
            .all()
        )
        return [
            {"client_name": result[0], "total_spent": float(result[1])}
            for result in results
        ]