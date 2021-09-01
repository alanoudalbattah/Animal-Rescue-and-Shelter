import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

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


class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    
    first_name = db.Column(db.String, nullable=False, unique=True)
    last_name = db.Column(db.String, nullable=False, unique=True)
    image_link = db.Column(db.String(500))
    email = db.Column(db.String(120))
    mobile = db.Column(db.String(120))
    age = db.Column(db.String(120), nullable=False)

    ''' relationship '''
    # Owner:Cat One-To-Many (1:M) Bidirectional relationship
    cat = db.relationship("Cat", back_populates=("owner"))
    # Owner:Interview One-To-Many (1:M) Bidirectional relationship
    interview = db.relationship("Adoption_Interview", back_populates=("owner"))

    def __init__(self, first_name, last_name, image_link, email, mobile, age):
        self.first_name = first_name
        self.last_name = last_name
        self.image_link = image_link
        self.email = email
        self.mobile = mobile
        self.age = age

    def details(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'image': self.image_link,
            'email': self.email,
            'mobile': self.mobile,
            'age': self.age,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Breed(db.Model):
    __tablename__ = 'breed'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    location_of_origin = db.Column(db.String(120))
    image_link = db.Column(db.String(500))

    ''' relationships '''
    # Breed:Cat One-To-Many (1:M) 
    cats = db.relationship("Cat", backref="breed", cascade="all, delete")
    #? CASCADE ALL, DELETE to delete the children (Shows) automatically before deleting the parent

    def __init__(self, name, location_of_origin, image_link):
        self.name = name
        self.location_of_origin = location_of_origin
        self.image_link = image_link

    def details(self):
        return {
            'id': self.id,
            'name': self.name,
            'location_of_origin': self.location_of_origin,
            'image': self.image_link,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Cat(db.Model):
    __tablename__ = 'cat'
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    vaccinated = db.Column(db.Boolean(), default=False)
    letter_box_trained = db.Column(db.Boolean(), default=False)
    note = db.Column(db.String(400))

    ''' relationships '''
    # Cat:Breed Many-To-One (M:1) 
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'))
    # Cat:Interview One-To-One (1:1)
    interview = db.relationship("Adoption_Interview", back_populates="cat")
    # Cat:Owner Many-To-One (M:1)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))



    def __init__(self, name, image_link, age, gender, vaccinated, letter_box_trained, note):
        self.name = name
        self.image_link = image_link
        self.age = age
        self.gender = gender
        self.vaccinated = vaccinated
        self.letter_box_trained = letter_box_trained
        self.note = note

    def details(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image_link,
            'age': self.age,
            'gender': self.gender,
            'vaccinated': self.vaccinated,
            'letter_box_trained': self.letter_box_trained,
            'note': self.note
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def update(self):
        db.session.commit()


class Adoption_Interview(db.Model):
    __tablename__ = 'interview'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.Time)

    ''' relationships '''
    # Interview:Cat One-To-One (1:1) Parent.child uselist src: https://docs.sqlalchemy.org/en/14/orm/relationship_api.html
    cat_id = db.Column(db.Integer, db.ForeignKey('cat.id'), nullable=False)
    cat = db.relationship("Cat", back_populates="interview", uselist=False)
    # Interview:Owner Many-To-One (M:1) Bidirectional behavior is added :)
    owner = db.relationship("Owner", back_populates="interview")
    

    def __init__(self, date, time):
        self.date = date
        self.time = time

    def details(self):
        return {
            'id': self.id,
            'date': self.date,
            'time': self.time,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()