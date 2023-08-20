from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(150),default="admin")
    password = db.Column(db.String(150),default="sha256$d6GCZDY8zefOLAyn$ef4cfa179185989e5f74a2b99d5736bb0362fc166799f5f6fedbe4e22e9109c2")