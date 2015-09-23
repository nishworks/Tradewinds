# -*-coding:utf8-*-

from flask import Flask, render_template
app = Flask(__name__)

__doc__ = """

        http://flask.pocoo.org/docs/0.10/quickstart/

        render_template renders the variables and html, returning plain text string.
        Notice how we directly return string in hello_world example
"""


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
    return 'Hello World! <br /> <a href="simple"> Simple template </a>'

if __name__ == '__main__':
    app.run()
