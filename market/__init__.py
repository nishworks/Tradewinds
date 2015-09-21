# -*-coding:utf8-*-

from flask import Flask
app = Flask(__name__)

__doc__ = """

        http://flask.pocoo.org/docs/0.10/quickstart/

"""


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

