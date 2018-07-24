"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect
from WebProject import app
from WebProject.forms import LoginForm, RegisterForm
import logging

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Renders the register page."""
    form = RegisterForm()
    if form.validate_on_submit():
        app.logger.info('Register requested for user {}, email={}'.format(
            form.username.data, form.email.data ))
        return redirect('/home')

    return render_template(
        'register.html', 
        title='Register',
        year=datetime.now().year,
        form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Renders the login page."""
    form = LoginForm()
    if form.validate_on_submit():
        app.logger.info('Login requested for user {}'.format(form.username.data))
        return redirect('/home')

    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        form=form)