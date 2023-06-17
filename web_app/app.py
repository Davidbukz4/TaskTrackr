#!/usr/bin/python3
""" Starts The TaskTrackr Web Application """
from models import storage
from models.user import User
from models.task import Task
from models.base_model import BaseModel
from os import environ
from uuid import uuid4
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_login import LoginManager, login_user, logout_user, login_required, current_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'holberton'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Configure the user loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return storage.get(User, user_id)

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

@app.route('/', strict_slashes=False, methods=['GET'])
def home():
    """ TaskTrackr homepage """
    return render_template('index.html', cache_id=uuid4())

@app.route('/signup', strict_slashes=False, methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        try:
            user = User(username=username, password=password, email=email)
            storage.new(user)
            storage.save()
            flash('Registration successful. Please log in.', 'info')
            return redirect(url_for('login'))
        except Exception as e:
            flash('Username or email already exists. Login instead', 'error')
    return render_template('signup.html', form=form, cache_id=uuid4())

@app.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = storage.getUserObj(User, username)
        if user and user.check_password(password):
            userDict = user.to_dict()
            login_user(user)
            return redirect(url_for('main', user_id=userDict['id']))
        else:
            flash('Invalid username or password. Please try again.', 'error')
    return render_template('login.html', form=form, cache_id=uuid4())

@app.route('/logout', strict_slashes=False, methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/main', strict_slashes=False, methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def main():
    user_id = current_user.get_id()
    return render_template('main.html', userId=user_id, cache_id=uuid4())

@app.route('/about', strict_slashes=False, methods=['GET'])
def about():
    return render_template('about.html', cache_id=uuid4())

@app.teardown_appcontext
def close(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, threaded=True)
