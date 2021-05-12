from app import db
from datetime import datetime

class User(db.Model):
    id = db. Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def __init__(self, username, email, phone):
        self.username = username
        self.email = email
        self.phone = phone
    
    def __repr__(self):
        return f'<User | {self.username}>'
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(300))
    date_created = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    phone_number = db.Column(db.String(10))
    
    def __init__(self, title, body, user_id, phone_number):
        self.title = title
        self.body = body
        self.user_id = user_id
        self.phone_number = phone_number
        
    def __repr__(self):
        return f'<Post | {self.title}>'