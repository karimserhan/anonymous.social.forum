"""
Database models for the flask application.
"""

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from WebProject import db, login
from hashlib import md5
from enum import IntFlag

class Gender(IntFlag):
    Male = 1
    Female = 2
    FTM = 4
    MTF = 8
    Fluid = 16
    # add latest 2018+ genders here

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(1000))
    gender = db.Column(db.Enum(Gender))
    gender_of_interests = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

# Used by flask-login to load user from db as they navigate through pages
# (ids of logged users stored in application memory).
@login.user_loader
def load_user(id):
    return User.query.get(int(id))