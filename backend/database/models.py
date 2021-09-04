import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

 # TODO: Models will include at least… 
 # Two classes with primary keys at at least two attributes each ✔️
 # [Optional but encouraged] One-to-many or many-to-many relationships between classes ✔️
 # src: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html for relationships :)

'''
setup_db(app):
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):

    database_name ='animal_shelter'
    default_database_path= "postgresql://{}:{}@{}/{}".format('postgres', 'postgres', 'localhost:5432', database_name)

    #? DATABASE_URL is the Heroku database URL, which will be generated with Heroku command and saved in setup.sh file
    #? With os.getenv(), if DATABASE_URL is empty, it will get default_data_path directly
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL', default_database_path)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.app = app
    db.init_app(app)

    Migrate(app, db)

'''
    drops the database tables and starts fresh
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


'''
    ...
'''
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    
    first_name = db.Column(db.String, nullable=False, unique=True)
    last_name = db.Column(db.String, nullable=False, unique=True)
    avatar = db.Column(db.String(500))
    email = db.Column(db.String(120))
    mobile = db.Column(db.String(120))
    age = db.Column(db.String(120), nullable=False)

    ''' relationship '''
    # User:Pet One-To-Many (1:M) 

    #! not usefull in the meantime
    # i will not make use of this attribute in the meantime due to limited time
    # however i will keep this line and relationship commented here for future uses :)
    # adopted_pets = db.relationship("Pet", backref="user")
        
    # User:Interview One-To-Many (1:M) 
    interviews = db.relationship("Adoption_Interview", backref="user", cascade='all, delete')

    def __init__(self, first_name, last_name, avatar, email, mobile, age):
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar
        self.email = email
        self.mobile = mobile
        self.age = age

    def __repr__(self):
        return f'<User {self.id} {self.first_name} {self.last_name}>'


    def details(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'avatar': self.avatar,
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


'''
    ...
    in the meantime Specie has only one tuple --> Cat
    However, this class has been created because pet can be either dog or cat.
'''
class Specie(db.Model):
    __tablename__ = 'specie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    ''' relationships '''
    # Specie:Breed One-To-Many (1:M) 

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Specie {self.id} {self.name}>'

    def details(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

'''
    ...
'''
# the Breed is a table not attribute to apply 2nd normal form :) 
# src: https://www.geeksforgeeks.org/second-normal-form-2nf/ 
class Breed(db.Model):
    __tablename__ = 'breed'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    image_link = db.Column(db.String(500))

    # CLI Example
    # from app import create_app, db, Breed, Pet, User, Adoption_Interview, Specie
    # create_app().app_context().push
    # db.create_all()
    # Breed("some name2","some img").insert()

    ''' relationships '''
    # Breed:Specie Many-To-One (M:1) 
    specie_id = db.Column(db.Integer, db.ForeignKey('specie.id'), nullable=False)
    specie = db.relationship("Specie", backref="specie", cascade='all, delete')
    # Breed:Pet One-To-Many (1:M) 

    def __init__(self, name, image_link):
        self.name = name
        self.image_link = image_link

    def __repr__(self):
        return f'<Breed {self.id} {self.name}>'

    def details(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image_link,
            'specie_id': self.specie_id,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

'''
    ...
'''
class Pet(db.Model):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(120), nullable=False, unique=True)
    image_link = db.Column(db.String(500), nullable=False)
    age_in_months = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    vaccinated = db.Column(db.Boolean(), default=False, nullable=False)
    letter_box_trained = db.Column(db.Boolean(), default=False, nullable=False)
    note = db.Column(db.String(400))

    ''' relationships '''
    # Pet:Breed Many-To-One (M:1) 
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'), nullable=False)
    breed = db.relationship("Breed", backref="pet")
    # Pet:Interview One-To-One (1:1)
    #* no need to implement anything here :)
    # Pet:User Many-To-One (M:1)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pet_owner = db.relationship("User", backref="user_pet")


    def __init__(self, name, image_link, age_in_months, gender, vaccinated, letter_box_trained, note):
        self.name = name
        self.image_link = image_link
        self.age_in_months = age_in_months
        self.gender = gender
        self.vaccinated = vaccinated
        self.letter_box_trained = letter_box_trained
        self.note = note


    def __repr__(self):
        return f'<Breed {self.id} {self.name}>'


    def details(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_link': self.image_link,
            'age_in_months': self.age_in_months,
            'gender': self.gender,
            'vaccinated': self.vaccinated,
            'letter_box_trained': self.letter_box_trained,
            'note': self.note,
            'breed_id': self.breed_id,
            'breed_name': self.breed.name,
            'user_id': self.owner_id,
            'owner_name': self.pet_owner.first_name+' '+self.pet_owner.last_name,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def update(self):
        db.session.commit()

'''
    ...
'''
class Adoption_Interview(db.Model):
    __tablename__ = 'interview'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.Time)

    ''' relationships '''
    # Pet:Interview One-To-One (1:1) Parent.child uselist src: https://docs.sqlalchemy.org/en/14/orm/relationship_api.html
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
    pet_2b_adopted = db.relationship("Pet", backref=db.backref("interview", uselist=False, cascade='all, delete'))
    # Interview:User Many-To-One (M:1) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    potential_owner = db.relationship("User", backref="interviews", cascade='all, delete')
    

    def __init__(self, date, time):
        self.date = date
        self.time = time

    def __repr__(self):
        return f'<Adoption_Interview {self.id} {self.pet_2b_adopted.name} {self.potential_owner.first_name} {self.date} {self.time}>'

    def details(self):
        return {
            'id': self.id,
            'date': self.date,
            'time': self.time,
            'pet':self.pet_id,
            'pet name': self.pet_2b_adopted.name, 
            'potential owner id': self.user_id,
            'potential owner name': self.potential_owner.first_name+' '+self.potential_owner.last_name,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()