from flask import Flask, render_template
from flask import request
import util

# * CONFIG
app = Flask(__name__)


@app.route('/')
def index():
    memes = []
    if 'q' in request.args:
        q = request.args['q']
        memes = util.getMemes(q)
        print(memes)
    return render_template('index.html', memes_list=memes)
