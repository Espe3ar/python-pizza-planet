from app.plugins import db

class OrderBeverage(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order._id'))
    beverage_price = db.Column(db.Float)
    beverage_id = db.Column(db.Integer, db.ForeignKey('beverage._id'))
    beverage = db.relationship('Beverage', backref=db.backref('order_beverage'))
