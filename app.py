from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime, timedelta

from prettytable import PrettyTable

# initiate the prettytable
x = PrettyTable()

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
    coffee_name = db.Column(db.String(100), nullable=False)
    batch_type = db.Column(db.String(50), nullable=False)
    batch_start_water_volume = db.Column(db.Float, nullable=False)
    batch_end_water_volume = db.Column(db.Float, nullable=True)
    batch_start_water_temperature = db.Column(db.Float, nullable=False)
    batch_end_water_temperature = db.Column(db.Float, nullable=True)
    batch_coffee_quantity = db.Column(db.Float, nullable=False)
    batch_start_date = db.Column(db.DateTime)
    batch_estimated_end_date = db.Column(db.DateTime)
    batch_actual_end_date = db.Column(db.DateTime)
    batch_expiration_date = db.Column(db.DateTime)
    batch_ph = db.Column(db.Float, nullable=True)

def new_batch(coffee_name: str,
              batch_type: str,
              batch_start_water_volume: float,
              batch_start_water_temperature: float,
              batch_coffee_quantity: float) -> None:
    """ Adds a new batch to the date base."""

    batch = Batch(coffee_name=coffee_name,
                  batch_type=batch_type,
                  batch_start_water_volume=batch_start_water_volume,
                  batch_start_water_temperature=batch_start_water_temperature,
                  batch_coffee_quantity=batch_coffee_quantity)
    
    db.session.add(batch)
    db.session.commit()

def get_batch_by_id(batch_id: int) -> None:
    """ Prints out the batch information by its id or batch number."""
    batch = Batch.query.filter_by(id=batch_id).first()
    x.align ='r'
    x.field_names = ['id',
                     'coffee_name',
                     'batch_type',
                     'batch_start_water_volume',
                     'batch_end_water_volume',
                     'batch_start_water_temperature',
                     'batch_end_water_temperature',
                     'batch_coffee_quantity',
                     'batch_start_date',
                     'batch_estimated_end_date',
                     'batch_actual_end_date',
                     'batch_expiration_date',
                     'batch_ph'
                     ]
   
    x.add_row(
        [batch.id,
        batch.coffee_name,
        batch.batch_type,
        batch.batch_start_water_volume,
        batch.batch_end_water_volume,
        batch.batch_start_water_temperature,
        batch.batch_end_water_temperature,
        batch.batch_coffee_quantity,
        batch.batch_start_date,
        batch.batch_estimated_end_date,
        batch.batch_actual_end_date,
        batch.batch_expiration_date,
        batch.batch_ph]
        )
    print(x)
    x.clear()

def get_batch():
    """Prints out the batch information of the entire database."""
    batches = Batch.query.all()
    x.field_names = ['id',
                     'coffee_name',
                     'batch_type',
                     'batch_start_water_volume',
                     'batch_end_water_volume',
                     'batch_start_water_temperature',
                     'batch_end_water_temperature',
                     'batch_coffee_quantity',
                     'batch_start_date',
                     'batch_estimated_end_date',
                     'batch_actual_end_date',
                     'batch_expiration_date',
                     'batch_ph'
                     ]
    for batch in batches:
        x.add_row(
            [batch.id,
            batch.coffee_name,
            batch.batch_type,
            batch.batch_start_water_volume,
            batch.batch_end_water_volume,
            batch.batch_start_water_temperature,
            batch.batch_end_water_temperature,
            batch.batch_coffee_quantity,
            batch.batch_start_date,
            batch.batch_estimated_end_date,
            batch.batch_actual_end_date,
            batch.batch_expiration_date,
            batch.batch_ph
            ]
            )
    print(x)
    x.clear()