# -*-coding:utf8-*-

from flask import Flask, render_template
app = Flask(__name__)

__doc__ = """

        http://flask.pocoo.org/docs/0.10/quickstart/
        Default template directory in flask is 'templates'
        Default directory in flask to keep static content like css, js and images is 'static'

"""


@app.route("/test")
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5])


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

