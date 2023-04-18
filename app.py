from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initiate the app
app = Flask(__name__)

# config the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICIATIONS'] = False
db = SQLAlchemy(app)

# database models
class Batch(db.Model):
    pass

class Product(db.Model):
    pass

# Association table
customer_order = db.Table('customer_order', )

class Customer(db.Model):
    pass

class Order(db.Model):
    pass

