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


    # Owner("AlAnoud","AlBattah","", "alanoudalbattah@outlook.com", "054211111", "23").insert()

    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    
    first_name = db.Column(db.String, nullable=False, unique=True)
    last_name = db.Column(db.String, nullable=False, unique=True)
    avatar = db.Column(db.String(500))
    email = db.Column(db.String(120))
    mobile = db.Column(db.String(120))
    age = db.Column(db.String(120), nullable=False)

    ''' relationship '''
    # Owner:Cat One-To-Many (1:M) Bidirectional relationship
    #adopted_cats = db.relationship("Cat", backref="cat_owner")
    
    # Owner:Interview One-To-Many (1:M) Bidirectional relationship
    #interviews_with = db.relationship("Adoption_Interview", backref="potential_owner")

    def __init__(self, first_name, last_name, avatar, email, mobile, age):
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar
        self.email = email
        self.mobile = mobile
        self.age = age

    def __repr__(self):
        return f'<Owner {self.id} {self.first_name} {self.last_name}>'


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

# the Breed is a table not attribute to apply 2nd normal form :) 
# src: https://www.geeksforgeeks.org/second-normal-form-2nf/ 
class Breed(db.Model):
    __tablename__ = 'breed'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    image_link = db.Column(db.String(500))

    # from app import create_app, db, Breed, Cat, Owner, Adoption_Interview
    # create_app().app_context().push
    # db.create_all()
    # Breed("some name2","some img").insert()

    ''' relationships '''
    # Breed:Cat One-To-Many (1:M) 
    #cats = db.relationship("Cat", backref="breed", lazy=True, cascade="all, delete")
    #? CASCADE ALL, DELETE to delete the children (Shows) automatically before deleting the parent

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

    # Cat("Hamoosh","https://catunited.com/wp-content/uploads/2020/03/2-1.png","12","Male",true,true,"Likes to play with a lazer :)").insert()

    __tablename__ = 'cat'
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    age_in_months = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    vaccinated = db.Column(db.Boolean(), default=False)
    letter_box_trained = db.Column(db.Boolean(), default=False)
    note = db.Column(db.String(400))

    ''' relationships '''
    # Cat:Breed Many-To-One (M:1) 
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'))
    breed = db.relationship("Breed", backref="cat")
    # Cat:Interview One-To-One (1:1)
    interview_id = db.Column(db.Integer, db.ForeignKey('interview.id'))
    interviews_for = db.relationship("Adoption_Interview", backref=db.backref("cat_2b_adopted", uselist=False))

    # Cat:Owner Many-To-One (M:1)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    cat_owner = db.relationship("Owner", backref="adopted_cat")



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
    # cat_id = db.Column(db.Integer, db.ForeignKey('cat.id'), nullable=False)
    # cat_2b_adopted = db.relationship("Cat", backref="interviews_for")

    # Interview:Owner Many-To-One (M:1) Bidirectional behavior is added :)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)
    potential_owner = db.relationship("Owner", backref="interviews")
    

    def __init__(self, date, time):
        self.date = date
        self.time = time

    def __repr__(self):
        return f'<Adoption_Interview {self.id} {self.cat_2b_adopted} {self.cat_2b_adopted} {self.date} {self.time}>'

    def details(self):
        return {
            'id': self.id,
            'date': self.date,
            'time': self.time,
            'cat':self.cat_id,
            'owner': self.owner_id,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()