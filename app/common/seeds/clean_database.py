from app import flask_app
from app.plugins import db

def clean_database():
    with flask_app.app_context():
        db.drop_all()
        
        db.create_all()
        
        print("Database cleaned and recreated.")

if __name__ == "__main__":
    clean_database()
