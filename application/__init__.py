from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv

app = Flask(__name__)

SECRET_KEY = os.urandom(32)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config["SECRET_KEY"] = SECRET_KEY
db = SQLAlchemy(app)

from application import routes