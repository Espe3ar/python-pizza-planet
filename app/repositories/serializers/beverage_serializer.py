from app.plugins import ma
from app.repositories.models.beverage import Beverage

class BeverageSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Beverage
        load_instance = True
        fields = ('_id', 'name', 'price')
