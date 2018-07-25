"""
Define the forms
"""

from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from WebProject.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=25)])
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=120), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Repeat Password', [DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min=6, max=25)])
    password = PasswordField('Password', [DataRequired(), Length(min=6, max=40)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login') 

class ProfileEditForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    about_me = StringField('About me')
    password_changed = BooleanField('PasswordChanged')
    password = PasswordField('Password', validators=[Length(min=6, max=40)])
    confirm = PasswordField('Repeat Password', [EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Save Changes')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None and user.id != current_user.id:
            raise ValidationError('Please use a different username.')