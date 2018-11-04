from flask import Flask, jsonify
from go import go_live

first_app = Flask(__name__)

@first_app.route('/')

def hello_world():
 #   return 'Hello world'
    return jsonify(Products=go_live())
  # print headerText
if __name__ == '__main__' :
    first_app.run()
