
from app.controllers.base import BaseController
from app.repositories.managers import BeverageManager


class BeverageController(BaseController):
    manager = BeverageManager