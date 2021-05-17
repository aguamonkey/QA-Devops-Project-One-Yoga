from application import db
from datetime import datetime

association_table = db.Table('association_table', db.Model.metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('move_id', db.Integer, db.ForeignKey('yoga_move.id')),
    db.Column('sequence_id', db.Integer, db.ForeignKey('yoga_sequence.id')))

class YogaMove(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    instruction = db.Column(db.String(200), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    sequences = db.relationship('YogaSequence', backref='move', secondary='association_table')

class YogaSequence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    time = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    moves = db.relationship('YogaMove', backref='sequence', passive_deletes = True, secondary='association_table')





