mkdir static
mkdir static/memes
cp processed/* static/memes/
FLASK_ENV=development FLASK_APP=app.py flask run