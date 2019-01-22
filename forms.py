from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import PasswordField, DateField
from wtforms import SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                             validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired() ])
    confirmPassword = PasswordField('Confrim Password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')