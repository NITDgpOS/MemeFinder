mkdir static
mkdir static/processed
cp processed/* static/processed/
FLASK_ENV=development FLASK_APP=app.py flask run