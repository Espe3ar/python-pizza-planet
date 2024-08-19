from app.plugins import ma
from app.repositories.models.order_ingredient import OrderIngredient
from .ingredient_serializer import IngredientSerializer

class OrderIngredientSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = OrderIngredient
        load_instance = True
        fields = (
            'ingredient_price',
            'ingredient'
        )
