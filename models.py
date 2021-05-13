from app import db, login
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from datetime import datetime

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    
    def __init__(self, username, email, password, phone):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.phone = phone
    
    def __repr__(self):
        return f'<User | {self.username}>'
    