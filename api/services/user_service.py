import email
from ..models import user_model
from api import db


def register_users(user):
    user_db = user_model.User(
                name=user.name,
                username=user.username,
                password=user.password,
                is_admin=user.is_admin
            )
    user_db.encrypt_password()
    db.session.add(user_db)
    db.session.commit()
    return user_db


def list_user_username(username):
    return user_model.User.query.filter_by(username=username).first()


def list_user_id(id):
    return user_model.User.query.filter_by(id=id).first()
# def list_users():
#     users = user_model.User.query.all()
#     return users