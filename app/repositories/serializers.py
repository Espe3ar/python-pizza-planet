from app.plugins import ma
from .models import Beverage, Ingredient, OrderBeverage, OrderIngredient, Size, Order


class IngredientSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Ingredient
        load_instance = True
        fields = ('_id', 'name', 'price')

class BeverageSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Beverage
        load_instance = True
        fields = ('_id', 'name', 'price')

class SizeSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Size
        load_instance = True
        fields = ('_id', 'name', 'price')


class OrderIngredientSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = OrderIngredient
        load_instance = True
        fields = (
            'ingredient_price',
            'ingredient'
        )

class OrderBeverageSerializer(ma.SQLAlchemyAutoSchema):

    beverage = ma.Nested(BeverageSerializer)

    class Meta:
        model = OrderBeverage
        load_instance = True
        fields = (
            'beverage_price',
            'beverage'
        )

class OrderSerializer(ma.SQLAlchemyAutoSchema):
    size = ma.Nested(SizeSerializer)
    ingredients = ma.Nested(OrderIngredientSerializer, many=True)
    beverages = ma.Nested(OrderBeverageSerializer, many=True)

    class Meta:
        model = Order
        load_instance = True
        fields = (
            '_id',
            'client_name',
            'client_dni',
            'client_address',
            'client_phone',
            'date',
            'total_price',
            'size',
            'ingredients',
            'beverages'
        )
