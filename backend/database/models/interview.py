from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()    

#? Difference between association models and association table
# " The association object pattern is a variant on many-to-many: it’s used when your association table contains
# additional columns beyond those which are foreign keys to the left and right tables. Instead of using the secondary
# argument, you map a new class directly to the association table. " src: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many


class Adoption_Interview(db.Model):
    __tablename__ = 'interview'
    id = db.Column(db.Integer, primary_key=True)

    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)
    
    date = db.Column(db.Date)
    time = db.Column(db.Time)

    ''' relationship '''
    # one-to-one Parent.child
    pet = db.relationship("Cat", back_populates="interview", uselist=False)
    # Many To One relationship parent=Owner child=interview Bidirectional relationship
    interview_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    interview = db.relationship("Owner", back_populates="interview")


    def __init__(self, date, time):
        self.date = date
        self.time = time

    def details(self):
        return {
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