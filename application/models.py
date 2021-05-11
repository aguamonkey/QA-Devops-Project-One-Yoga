from application import db
from datetime import datetime

class Yogamove(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    instruction = db.Column(db.String(200), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())