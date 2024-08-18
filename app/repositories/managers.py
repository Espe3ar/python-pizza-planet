from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column, func

from .models import Beverage, Ingredient, Order, OrderBeverage, OrderIngredient, Size, db
from .serializers import (BeverageSerializer, IngredientSerializer, OrderSerializer,SizeSerializer, ma)


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []

class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer
    
    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []

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
            cls.session.add_all((
            OrderIngredient(
                order_id=new_order._id,
                ingredient_id=ingredient._id,
                ingredient_price=ingredient.price,
            ) for ingredient in ingredients
        ))
            cls.session.add_all((
            OrderBeverage(
                order_id=new_order._id,
                beverage_id=beverage._id,
                beverage_price=beverage.price,
            ) for beverage in beverages
        ))
            cls.session.refresh(new_order)
            cls.session.commit()
            return cls.serializer().dump(new_order)
        except Exception as e:
            cls.session.rollback()
            raise e

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')

class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()

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
                func.cast(func.strftime("%m", Order.date), db.Integer),
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