from flask import Flask, render_template
from flask import request
import util

# * CONFIG
app = Flask(__name__)


@app.route('/')
def index():
    memes = []
    if 'q' in request.form:
        q = request.form ['q']
        memes = util.getMemes(q)
    return render_template('index.html', memes=memes)
