from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    description = StringField("Move Name:", validators=[DataRequired()])
    instruction = StringField("Move Instructions:", validators=[DataRequired()])
    difficulty = SelectField("Move Difficulty:", choices=["Beginner", "Intermediate", "Advanced"])
    submit = SubmitField('Add Task')