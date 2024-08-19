from datetime import datetime
from app.plugins import db

class Order(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(80))
    client_dni = db.Column(db.String(10))
    client_address = db.Column(db.String(128))
    client_phone = db.Column(db.String(15))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    total_price = db.Column(db.Float)
    size_id = db.Column(db.Integer, db.ForeignKey('size._id'))

    size = db.relationship('Size', backref=db.backref('size'))
    ingredients = db.relationship('OrderIngredient', backref=db.backref('order_ingredient'), cascade="all, delete-orphan")
    beverages = db.relationship('OrderBeverage', backref=db.backref('order_beverage'), cascade="all, delete-orphan")
