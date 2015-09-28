# -*-coding:utf8-*-
import logging
from logging import StreamHandler

from flask import Flask, render_template, request
from flask import session, url_for, redirect, flash
from auth import AuthUser
from firm import Firms

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
        return render_template('home.html')
    return response('You are not logged in','login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('home'))
    if not request.method == 'POST':
        return render_template('register.html')
    username = request.form.get('username')
    if username == None:
        return response('Username is Invalid','register')
    authUser = AuthUser(username)
    if authUser.exists:
        return response('User already exists','register')
    if authUser.addUser(request.form):
        return response('Registration successful','login')
    return response('Internal Error','register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))
    if not request.method == 'POST':
        return render_template('login.html')
    username = request.form.get('username')
    if username is None:
        return response('Username is Invalid','login')
    authUser = AuthUser(username)
    if not authUser.exists:
        return response('Username is not registered','login')
    instance_id = authUser.authenticate(request.form.get('password'))
    if instance_id is None:
        return response('Invalid password','login')
    session['username'] = request.form['username']
    session['userid'] = instance_id
    return response(str("Welcome " + session['username']),'home')


@app.route('/addfirm', methods=['GET', 'POST'])
def add_firm():
    if 'username' not in session:
        return response('You are not logged in','login')
    if not request.method == 'POST':
        return render_template('add_firm.html')
    name = request.form.get('name')
    if name is None:
        return response('Name is invalid','add_firm')
    msg = Firms(session['userid'],name).addFirm(request.form)
    return response(msg,'home')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return response('Logout successful','login')

def response(msg, url):
    flash(msg)
    return redirect(url_for(url))



if __name__ == '__main__':
    app.run()
