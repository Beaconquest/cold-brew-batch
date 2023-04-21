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
    A class to represent a batch information for cold brew coffee, in the database.
    
    Attributes
    __________

    """
    id = db.Column(db.Integer, primary_key=True)
    coffee_name = db.Column(db.String(100), nullable=False )
    batch_type = db.Column(db.String(50), nullable=False)
    batch_start_water_volume = db.Column(db.Float, nullable=False)
    batch_end_water_volume = db.Column(db.Float, nullable=False)
    batch_start_water_temperature = db.Column(db.Float, nullable=False)
    batch_end_water_temperature = db.Column(db.Float, nullable=False)
    batch_coffee_quantity = db.Column(db.Float, nullable=False)
    batch_start_date = db.Column(db.DateTime)
    batch_estimated_end_date = db.Column(db.DateTime)
    batch_actual_end_date = db.Column(db.DateTime)
    Batch_expiration_date = db.Column(db.DateTime)
    batch_ph = db.Column(db.Float, nullable=False)

