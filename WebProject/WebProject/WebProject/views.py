"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import logging
from WebProject import app, db
from WebProject.forms import LoginForm, RegistrationForm
from WebProject.models import User

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    if current_user.is_authenticated:
        return redirect(url_for('feed'))
    else:
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
        year=datetime.now().year
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Renders the about page and registers new users for POST requests."""
    if current_user.is_authenticated:
        return redirect(url_for('feed'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        login_user(user, remember=False)
        return redirect(url_for('feed'))
    return render_template(
        'register.html', 
        title='Register',
        year=datetime.now().year,
        form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Renders the login page and authenticates POST requests."""
    if current_user.is_authenticated:
        return redirect(url_for('feed'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # if the user was redirected to /login from a login-protected page, redirect to the original page
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('feed')
        return redirect(next_page)
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/feed')
@login_required
def feed():
    """Renders the feed page."""
    return render_template(
        'feed.html',
        title='Home Page',
        year=datetime.now().year)

@app.route('/user/<userid>')
@login_required
def user(userid):
    """Renders the user page."""
    user = User.query.filter_by(id=userid).first_or_404()
    # TODO: authorization
    return render_template(
        'user_overview.html',
        title='Profile',
        year=datetime.now().year,
        user=user)

@app.route('/activity/<userid>')
@login_required
def activity(userid):
    """Renders the user page."""
    user = User.query.filter_by(id=userid).first_or_404()
    # TODO: authorization
    return render_template(
        'user_activity.html',
        title='Activity',
        year=datetime.now().year,
        user=user)

@app.route('/conversation/<userid>')
@login_required
def conversation(userid):
    """Renders the user page."""
    user = User.query.filter_by(id=userid).first_or_404()
    # TODO: make sure they match first before viewing profiles!
    return render_template(
        'user_conversation.html',
        title='Conversation',
        year=datetime.now().year,
        user=user)

@app.route('/matches/<userid>')
@login_required
def matches(userid):
    """Renders the user page."""
    user = User.query.filter_by(id=userid).first_or_404()
    # TODO: authorization
    return render_template(
        'user_matches.html',
        title='Matches',
        year=datetime.now().year,
        user=user)

@app.route('/editprofile/<userid>')
@login_required
def editprofile(userid):
    """Renders the user page."""
    user = User.query.filter_by(id=userid).first_or_404()
    # TODO: authorization
    return render_template(
        'user_edit.html',
        title='Edit Profile',
        year=datetime.now().year,
        user=user)