# -*-coding:utf8-*-
import logging
from logging import StreamHandler

from flask import Flask, render_template, request
from flask import session, url_for, redirect
from auth import AuthUser

app = Flask(__name__)

__doc__ = """

        http://flask.pocoo.org/docs/0.10/quickstart/

        render_template renders the variables and html, returning plain text string.
        Notice how we directly return string in hello_world example
"""
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Setup logging to see error messages on terminal
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(StreamHandler())

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', resp=str("Welcome " + session['username']))
    return render_template('login.html', resp="You are not logged in")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('home'))
    if not request.method == 'POST':
        return render_template('register.html')
    username = request.form.get('username')
    if username is None:
        return render_template('register.html', resp="Username is invalid")
    authUser = AuthUser(username)
    if authUser.exists:
        return render_template('register.html', resp='User already exists')
    if authUser.addUser(request.form):
        return render_template('register.html', resp='Registration successful')
    return render_template('register.html', resp='Internal Error')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if not request.method == 'POST':
        return render_template('login.html')
    if 'username' in session:
        return redirect(url_for('home'))
    username = request.form.get('username')
    if username is None:
        return render_template('login.html', resp="Username is Invalid")
    authUser = AuthUser(username)
    if not authUser.exists:
        return render_template('login.html', resp="Username is not registered")
    instance_id = authUser.authenticate(request.form.get('password'))
    if instance_id is None:
        return render_template('login.html', resp='Invalid password')
    session['username'] = request.form['username']
    session['userid'] = instance_id
    return redirect(url_for('home'))


@app.route('/addfirm', methods=['GET', 'POST'])
def add_firm():
    if 'username' not in session:
        return render_template('login.html', resp="You are not logged in")
    if not request.method == 'POST':
        return render_template('add_firm.html')
    name = request.form.get('name')
    if name is None:
        return render_template('add_firm.html', resp="name is invalid")
    authUser = AuthUser(session['username'])
    msg = authUser.addFirm(request.form)
    return render_template('home.html', resp=msg)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('login.html', resp="Logout successful!")


if __name__ == '__main__':
    app.run()
