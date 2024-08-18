import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
import random
from datetime import datetime, timedelta

from app import flask_app
from faker import Faker
from app import flask_app
from app.plugins import db
from app.repositories.models import (
    Beverage,
    Ingredient,
    Order,
    OrderBeverage,
    OrderIngredient,
    Size,
)

fake = Faker()

def create_ingredients():
    ingredients = [
        Ingredient(name='Cheese', price=1.0),
        Ingredient(name='Pepperoni', price=1.5),
        Ingredient(name='Mushrooms', price=0.8),
        Ingredient(name='Onions', price=0.3),
        Ingredient(name='Sausage', price=1.2),
        Ingredient(name='Bacon', price=1.7),
        Ingredient(name='Black Olives', price=0.7),
        Ingredient(name='Green Peppers', price=0.6),
        Ingredient(name='Pineapple', price=0.9),
        Ingredient(name='Spinach', price=0.4)
    ]
    
    for ingredient in ingredients:
        db.session.add(ingredient)
    
    db.session.commit()

def create_sizes():
    sizes = [
        Size(name='S', price=2.0),
        Size(name='M', price=4.0),
        Size(name='L', price=6.0),
        Size(name='XL', price=8.0),
        Size(name='XXL', price=10.0)
    ]
    
    for size in sizes:
        db.session.add(size)
    
    db.session.commit()

def create_beverages():
    beverages = [
        Beverage(name='Coke', price=1.5),
        Beverage(name='Diet Coke', price=1.5),
        Beverage(name='Sprite', price=1.5),
        Beverage(name='Water', price=1.0),
        Beverage(name='Juice', price=2.0)
    ]
    
    for beverage in beverages:
        db.session.add(beverage)
    
    db.session.commit()

def calculate_total_price(order):
    total_price = order.size.price
    for ingredient in order.ingredients:
        total_price += ingredient.ingredient.price
    for beverage in order.beverages:
        total_price += beverage.beverage.price
    return total_price

def create_orders():
    sizes = Size.query.all()
    ingredients = Ingredient.query.all()
    beverages = Beverage.query.all()
    date_order = fake.date_time_between(
            start_date=datetime(2024, 1, 1),
            end_date=datetime.now()
        )
    for _ in range(100):
        order = Order(
            client_name=fake.name(),
            client_dni=fake.ssn(),
            client_address=fake.address(),
            client_phone=fake.phone_number(),
            date=date_order,
            size=random.choice(sizes)
        )
        
        num_ingredients = random.randint(1, 5)
        num_beverages = random.randint(1, 3)
        
        for _ in range(num_ingredients):
            ingredient = random.choice(ingredients)
            order_ingredient = OrderIngredient(
                ingredient=ingredient,
                ingredient_price=ingredient.price
            )
            order.ingredients.append(order_ingredient)
        
        for _ in range(num_beverages):
            beverage = random.choice(beverages)
            order_beverage = OrderBeverage(
                beverage=beverage,
                beverage_price=beverage.price
            )
            order.beverages.append(order_beverage)
        
        order.total_price = calculate_total_price(order)
        
        db.session.add(order)
    
    db.session.commit()


if __name__ == "__main__":
    with flask_app.app_context():
        db.create_all()
        create_sizes()
        create_ingredients()
        create_beverages()
        create_orders()
