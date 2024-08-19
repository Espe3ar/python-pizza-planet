from app.plugins import ma
from app.repositories.models.size import Size

class SizeSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Size
        load_instance = True
        fields = ('_id', 'name', 'price')
