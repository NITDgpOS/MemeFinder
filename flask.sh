mkdir server/static
mkdir server/static/memes
cp processed/* server/static/memes/
FLASK_ENV=development FLASK_APP=server/app.py flask run