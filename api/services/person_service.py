from ..models import person_model
from api import db

def register_person(person):
    person_db = person_model.Person(name=person.name)
    db.session.add(person_db)
    db.session.commit()
    return person_db

def list_persons():
    persons = person_model.Person.query.all()
    return persons

def list_person_by_id(id):
    person = person_model.Person.query.filter_by(id=id).first()
    return person

def update_person(old_person, new_person):
    old_person.name = new_person.name
    db.session.commit()

def delete_person(person):
    db.session.delete(person)
    db.session.commit()


