from flask import Flask, render_template
from flask import request
from .util import getMemes

# CONFIG
app = Flask(__name__)


@app.route('/')
def index():
    """ 
        The whole website works on a single route.
        If the route gets any GET requests with queries in the URL,
        we send them the search page with memes.
    """
    if 'q' in request.args:
        q = request.args['q']
        memes = getMemes(q)
    else:
        memes = None

    return render_template('index.html', memes_list=memes)
