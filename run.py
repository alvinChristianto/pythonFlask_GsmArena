from flask import Flask
first_app = Flask(__name__)

@first_app.route('/')

def hello_world():
    return 'Hello world'

if __name__ = '__main__' :
    first_app.run()
