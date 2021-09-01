import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy() 

'''
setup_db(app):
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):

    database_name ='animal_shelter'
    default_database_path= "postgresql://{}:{}@{}/{}".format('postgres', 'postgres', 'localhost:5432', database_name)

    #? DATABASE_URL is the Heroku database URL, which will be generated with Heroku command and saved in setup.sh file
    #? With os.getenv(), if DATABASE_URL is empty, it will get default_data_path directly
    database_path = os.getenv('DATABASE_URL', default_database_path)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.app = app
    db.init_app(app)
    db.create_all()

    Migrate(app, db)

'''
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

 # TODO: Models will include at least… 
 # Two classes with primary keys at at least two attributes each ✅
 # [Optional but encouraged] One-to-many or many-to-many relationships between classes ✅
 # src: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html for relationships :)
