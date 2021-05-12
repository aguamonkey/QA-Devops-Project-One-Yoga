from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    description = StringField("Move Name:", validators=[DataRequired()])
    instruction = StringField("Move Instructions:", validators=[DataRequired()])
    difficulty = SelectField("Move Difficulty:", choices=["Beginner", "Intermediate", "Advanced"])
    submit = SubmitField('Create Move')

class TaskFormTwo(FlaskForm):
    name = StringField("Sequence Name:", validators=[DataRequired()])
    time = IntegerField("Minutes to complete (number required):", validators=[DataRequired()])
    difficulty = SelectField("Sequence Difficulty:", choices=["Beginner", "Intermediate", "Advanced"])
    instruction = SelectField("Add new instruction:", choices=[])
    submit = SubmitField('Create Sequence')
    add_instruction = SubmitField('Add Instruction')