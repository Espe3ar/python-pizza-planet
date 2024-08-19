from sqlalchemy.sql import text, column
from .base_manager import BaseManager

class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()
