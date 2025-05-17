from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello all, this site is created only for demo purposes :) (Only for testing). Testing for the second version '

@app.route('/health')
def health():
    return 'Server is up and running'
