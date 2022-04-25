# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography',validators=[InputRequired()])
    user_photo= FileField('Profile Photo',validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
    
class CarForm(FlaskForm):
    description = StringField('description', validators=[InputRequired()])
    make = StringField('make', validators=[InputRequired()])
    colour = StringField('colour', validators=[InputRequired()])
    year = StringField('year', validators=[InputRequired()])
    transmission = StringField('transmission', validators=[InputRequired()])
    car_type = StringField('car_type', validators=[InputRequired()])
    price = StringField('price', validators=[InputRequired()])
    photo = FileField('Car Photo', validators=[FileRequired(), FileAllowed(['jpg','png'],'Image only!')])
 

