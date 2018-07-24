"""
Database models for the flask application.
"""

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from WebProject import db, login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Used by flask-login to load user from db as they navigate through pages
# (ids of logged users stored in application memory).
@login.user_loader
def load_user(id):
    return User.query.get(int(id))