from app.plugins import ma
from app.repositories.models.order import Order
from .size_serializer import SizeSerializer
from .order_ingredient_serializer import OrderIngredientSerializer
from .order_beverage_serializer import OrderBeverageSerializer

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
