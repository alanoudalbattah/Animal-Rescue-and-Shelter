import os
from flask_sqlalchemy import SQLAlchemy

 # TODO: Models will include at least… 
 # Two classes with primary keys at at least two attributes each ✔️
 # [Optional but encouraged] One-to-many or many-to-many relationships between classes ✔️
 # src: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html for relationships :)

database_name ='animal_shelter'
database_path= "postgresql://{}:{}@{}/{}".format('postgres', 'postgres', 'localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app):
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):

    #? DATABASE_URL is the Heroku database URL, which will be generated with Heroku command and saved in setup.sh file
    #? With os.getenv(), if DATABASE_URL is empty, it will get default_data_path directly
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL', database_path)
    #app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL').replace("://", "ql://", 1)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.app = app
    db.init_app(app)

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
    email = db.Column(db.String(120))
    mobile = db.Column(db.String(120))
    age = db.Column(db.String(120), nullable=False)

    ''' relationship '''
    # Interview:User Many-To-One (M:1) interview --> parent, user --> child
    #* no need to do anything here :)

    # User:Pet One-To-Many (1:M)  user --> parent, pet --> child #! X
    # i will not make use of this attribute in the meantime due to limited time
    # however i will keep this line and relationship commented here for future uses :)
    #adopted_pets = db.relationship("Pet", backref="user")
    
    def __init__(self, first_name, last_name, email, mobile, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile = mobile
        self.age = age

    def __repr__(self):
        return f'<User {self.id} {self.first_name} {self.last_name}>'


    def details(self):
        return {
            'id': self.id,
            'name': self.first_name +' '+ self.last_name,
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
    in the meantime Specie has only one tuple --> Cat
    However, this class has been created because pet can be either dog or cat or any rescued animals.
'''
class Specie(db.Model):
    __tablename__ = 'specie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    ''' relationships '''
    # Breed:Specie Many-To-One (M:1) parent --> Breed, child --> specie
    # no need to implement anything here for this relationship :)
 
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
    breed objects represent Hamalaya, Sherazi, Rag Doll for a specie (Cat)
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
    
    # Breed:Specie Many-To-One (M:1) parent --> Breed, child --> specie
    specie_id = db.Column(db.Integer, db.ForeignKey('specie.id'), nullable=False)
    specie = db.relationship("Specie", backref="breed_specie")

    #?
    # i think for the parent to be a breed is conceptually wrong...
    # however,
    # i did this relationship to apply nullable=False on the Foreign Key
    # because a breed can't be created without a specie first
    # if there is another way to apply this constraint please don't hasetatie to inform me
    # thank you :) 
    # previous relationship: # Specie:Breed One-To-Many (1:M) Specie --> parent, Breed --> child.
    # many --> 1..* not 0..*

    # Breed:Pet One-To-Many (1:M) Breed --> parent, Pet --> child.
    pets = db.relationship("Pet", backref="breed_pet", cascade="all, delete")

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
    pets are animals that has been rescued by the shelter and 
    and created for adoption interview oppetunities :)
'''
class Pet(db.Model):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    age_in_months = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    vaccinated = db.Column(db.Boolean(), default=False, nullable=False)
    letter_box_trained = db.Column(db.Boolean(), default=False, nullable=False)
    note = db.Column(db.String(400))

    ''' relationships '''
    # Interview:Pet One-To-One (1:1) interview --> parent, pet --> child 
    #* no need to implement anything here :)
    
    # Pet:Breed Many-To-One (M:1)  parent --> Pet, child --> Breed
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'), nullable=False)
    breed = db.relationship("Breed", backref="pet_breed")
    # many --> 1..* not 0..*
    #? same as previous relation with:
    # Breed:Specie Many-To-One (M:1) parent --> Breed, child --> specie
    
    # Pet:User Many-To-One (M:1) pet --> parent, user --> child #! X
    # this line and relationship commented here for future uses :)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # pet_owner = db.relationship("User", backref="user_pet")


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
            'breed_name': self.breed.name
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
    
    date = db.Column(db.Date, nullable=False) # --> datetime.date() 
    # src: https://docs.python.org/3/library/datetime.html
    time = db.Column(db.DateTime, nullable=False) # --> datetime.datetime() 
    # src: https://docs.python.org/3/library/datetime.html

    ''' relationships '''
    # Interview:Pet One-To-One (1:1) interview --> parent, pet --> child 
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    pet_2b_adopted = db.relationship("Pet", backref=db.backref("interview", uselist=False))
    
    # Interview:User Many-To-One (M:1) interview --> parent, user --> child
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    potential_owner = db.relationship("User", backref="interviews")
    

    def __init__(self, date, time):
        self.date = date
        self.time = time

    def __repr__(self):
        return f'<Adoption_Interview {self.id} {self.date.strftime("%m/%d/%Y")} {self.time.strftime("%H:%M")}>' # 

    def details(self):
        return {
            'id': self.id,
            'date': self.date.strftime("%m/%d/%Y"),
            'time': self.time.strftime("%H:%M"),
            'pet_id': self.pet_id,
            'interview for': self.pet_2b_adopted.name,
            'user_id': self.user_id,
            'interview with': self.potential_owner.first_name +' '+ self.potential_owner.last_name
        }
    #src: https://www.codegrepper.com/code-examples/python/convert+datetime+object+into+string+sqlalchemy

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()