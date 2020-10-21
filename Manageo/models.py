from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column('user_id', db.Integer, primary_key = True)
    user_first_name = db.Column('user_first_name', db.String(50))
    user_last_name = db.Column('user_last_name', db.String(50))
    mdp_hash = db.Column('mdp_hash', db.String(70))
    user_email = db.Column('user_email', db.String(320), unique = True)
    user_adress = db.Column('user_adress', db.String())
    user_phone = db.Column('user_phone', db.String(20))

