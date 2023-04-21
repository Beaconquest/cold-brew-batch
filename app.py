from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime, timedelta

# initiate the app
app = Flask(__name__)

# config the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICIATIONS'] = False
db = SQLAlchemy(app)

# database models
class Batch(db.Model):
    """
    A class to represent a batch of cold brew coffee, in the database.
    
    Attributes
    __________

    """
    id = db.Column(db.Integer, primary_key=True)
    coffee_name = db.Column(db.String(100), nullable=False )
    batch_water_volume = db.Column(db.Float, nullable=False)
    batch_start_date = db.Column(db.DateTime)
    batch_end_date = db.Column(db.DateTime)


class Product(db.Model):
    """
    A class to represent a product of cold brew coffee, in the database.
    """
    id = db.Column(db.Integer, primary_key=True)

# Association table
customer_order = db.Table('customer_order', )

class Customer(db.Model):
    """
    A class to represent a customer or vendor of cold brew coffee, in the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(5), nullable=False)
    email = db.Column(db.String(250), nullable=False)


class Order(db.Model):
    """
    A class to represent an order of cold brew coffee, in the database.
    """
    id = db.Column(db.Integer, primary_key=True)

