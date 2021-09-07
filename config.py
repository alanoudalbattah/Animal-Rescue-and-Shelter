import os

#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
#! replaced due to deprecation in the changing of the dialect 
#src: https://stackoverflow.com/questions/66690321/flask-and-heroku-sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
SQLALCHEMY_TRACK_MODIFICATIONS = False
