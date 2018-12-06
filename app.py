from flask import Flask, render_template, send_from_directory
from flask import request
from lib.util import get_memes

# CONFIG
app = Flask(__name__)
app.config['MEMES_DIRECTORY'] = 'processed'


@app.route('/')
def index():
    """ 
        The whole website works on a single route.
        If the route gets any GET requests with queries in the URL,
        we send them the search page with memes.
    """
    if 'q' in request.args:
        q = request.args['q']
        memes = get_memes(q)
    else:
        memes = []

    return render_template('index.html', memes_list=memes)


@app.route('/processed/<path:filename>')
def get_processed_meme(filename):
    """
        Since in the current version of the application we store the processed image files,
        this function serves those image files to processed/ url.
    """
    return send_from_directory(app.config['MEMES_DIRECTORY'], filename)
