#!/usr/bin/python3
""" Starts The TaskTrackr Web Application """
from models import storage
from models.user import User
from models.task import Task
from models.base_model import BaseModel
from os import environ
from uuid import uuid4
from flask import Flask, render_template, redirect
from flask import url_for, request, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'holberton'


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
        user = User(username=username, password=password, email=email)
        storage.new(user)
        storage.save()
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form, cache_id=uuid4())

@app.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        userObj = storage.getUserObj(User, username)
        if userObj and userObj.check_password(password):
            user = userObj.to_dict()
            session['username'] = user['username']
            return redirect(url_for('main', user_id=user['id']))
        else:
            flash('Invalid username or password. Please try again.')
    return render_template('login.html', form=form, cache_id=uuid4())

@app.route('/main', strict_slashes=False,
           methods=['GET', 'POST', 'PUT', 'DELETE'])
def main():
    if 'username' in session:
        user_id = request.args.get('user_id')
        return render_template('main.html', 
                               userId=user_id,
                               cache_id=uuid4())
    else:
        return redirect(url_for('/login'))

@app.teardown_appcontext
def close(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
