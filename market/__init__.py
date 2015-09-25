# -*-coding:utf8-*-

from flask import Flask, render_template, request
from flask import session, url_for, redirect
app = Flask(__name__)

__doc__ = """

        http://flask.pocoo.org/docs/0.10/quickstart/

        render_template renders the variables and html, returning plain text string.
        Notice how we directly return string in hello_world example
"""
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/simple')
def template_example():
    return render_template('simple_template.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5])

@app.route('/candidate')
def candidate_one():
    return render_template('index.html')


@app.route('/nicer')
def another_template_example():
    return render_template('nicer.html')


@app.route('/')
def hello_world():
    return 'Hello World! <br /> <a href="/login"> Login </a>'

@app.route('/login')
def login_form():
    return render_template('login.html')

@app.route('/home')
def home():
	if 'username' in session:
		return render_template('home.html', user=session['username'])
	return render_template('login.html', resp="You are not logged in")    

@app.route('/authenticate', methods=['POST'])
def login():
	if request.form['username'] == 'nik' and request.form['password'] == 'nikh':
		print request.form['username']
		session['username'] = request.form['username']
		return redirect(url_for('home'))
	else:
		return render_template('login.html', resp="Wrong username and password,try again!")    		

@app.route('/logout')
def logout():
	session.pop('username', None)
	return render_template('login.html', resp="Logout successful!")
 

if __name__ == '__main__':
    app.run()
