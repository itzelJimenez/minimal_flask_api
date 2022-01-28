import time

import redis
from flask import Flask, request, jsonify


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

# Variables
@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/<string:name>/')
def hello_name(name):
    return "Hello " + name

# Return JSON Serializable Output
## dictionary objects:
@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    return jsonify({'name':'Jimit',
                    'address': 'Street 24'})

## serialize lists and tuples to JSON Response.
@app.route('/numbers/')
def print_list():
    return jsonify(list(range(5)))

# Redirection Behaviour
## Flask redirects you to the URL with the trailing slash.
@app.route('/home/')
def home():
    return "Home page"

## If you access the URL with the trailing slash, then it will result in status 404 Not Found.
@app.route('/example/contact')
def contact():
    return "Contact page"

# Return Status Code
@app.route('/teapot/')
def teapot():
    return "Would you like some tea?", 418

# Before Request
@app.before_request
def before():
    print("This is executed BEFORE 1 each request.")
    
@app.route('/before/request')
def before_request():
    return ">>> Hello World!"

### Request data
@app.route('/foo', methods=['POST']) 
def create_person():
    data = request.json
    # Save data or something
    return jsonify({"status": 200, "data": data})