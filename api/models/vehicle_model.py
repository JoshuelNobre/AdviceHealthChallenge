from api import db
from ..models import person_model


class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    model = db.Column(db.String(50), nullable=False)
    collor = db.Column(db.String(100), nullable=False)


    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    person = db.relationship(person_model.Person, backref=db.backref("vehicle", lazy="dynamic"))

