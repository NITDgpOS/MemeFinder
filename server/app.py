from flask import Flask, url_for

# * CONFIG
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'
