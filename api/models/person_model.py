from api import db


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
