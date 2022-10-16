from re import T
from api import ma
from ..models import user_model
from marshmallow import fields


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = user_model.User
        load_instance = True
        fields = ("id", "name", "username", "password", "is_admin")

    name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    is_admin = fields.Boolean(required=True)

