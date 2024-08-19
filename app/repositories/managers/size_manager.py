from .base_manager import BaseManager
from app.repositories.models.size import Size
from app.repositories.serializers.size_serializer import SizeSerializer

class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer