from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DecimalField, SelectField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed

class AddPropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    bedrooms = IntegerField('Number of Bedrooms', validators=[InputRequired()])
    bathrooms = IntegerField('Number of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired()])
    property_type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
