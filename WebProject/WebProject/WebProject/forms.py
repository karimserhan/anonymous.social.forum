"""
Define the forms
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = StringField(
        'Email', validators=[DataRequired(), Length(min=6, max=120), Email()]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min=6, max=25)])
    password = PasswordField('Password', [DataRequired(), Length(min=6, max=40)])
    submit = SubmitField('Register')