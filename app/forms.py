from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired


selection_type = [('House', 'House'), ('Apartment', 'Apartment')]

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    bedrooms = StringField('Amount of Bedrooms', validators=[DataRequired()])
    bathrooms = StringField('Amount of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    type = SelectField('Property Type', choices=selection_type)
    description = TextAreaField('Property Description', validators=[DataRequired()])
    photo = FileField('File', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images Only!'])])