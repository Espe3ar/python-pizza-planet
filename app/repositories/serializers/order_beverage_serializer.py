from app.plugins import ma
from app.repositories.models.order_beverage import OrderBeverage
from .beverage_serializer import BeverageSerializer

class OrderBeverageSerializer(ma.SQLAlchemyAutoSchema):

    beverage = ma.Nested(BeverageSerializer)

    class Meta:
        model = OrderBeverage
        load_instance = True
        fields = (
            'beverage_price',
            'beverage'
        )