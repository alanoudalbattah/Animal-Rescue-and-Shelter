from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    
    first_name = db.Column(db.String, nullable=False, unique=True)
    last_name = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String(120))
    mobile = db.Column(db.String(120))
    age = db.Column(db.String(120), nullable=False)

    ''' relationship '''
    # One To Many relationship parent=Owner child=Pet Bidirectional relationship
    pet = db.relationship("Cat", back_populates=("owner"))
    # One To Many relationship parent=Owner child=interview Bidirectional relationship
    interview = db.relationship("Adoption_Interview", back_populates=("owner"))

    
    def __init__(self, first_name, last_name, email, mobile, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile = mobile
        self.age = age

    def details(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
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