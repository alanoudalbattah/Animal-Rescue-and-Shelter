from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()      

class breed(db.Model):
    __tablename__ = 'breed'
    id = db.Column(db.Integer, primary_key=True)
    breed_name= db.Column(db.String(50))


class Cat(db.Model):
    __tablename__ = 'cat'
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    vaccinated = db.Column(db.Boolean(), default=False)
    letter_box_trained = db.Column(db.Boolean(), default=False)
    note = db.Column(db.String(400))

    # one-to-one
    interview = db.relationship("Adoption_Interview", back_populates="cat")
    # Many To One relationship parent=Owner child=Pet Bidirectional relationship
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    owner = db.relationship("Owner", back_populates="cat")

    def __init__(self, first_name, last_name, email, mobile, city, country, age):
        self.first_name = first_name

    def details(self):
        return {
            'id': self.id,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def update(self):
        db.session.commit()
