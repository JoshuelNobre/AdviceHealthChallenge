from api import ma
from ..models import user_model
from marshmallow import fields


class LoginSchema(ma.SQLAlchemySchema):
    class Meta:
        model = user_model.User
        load_instance = True
        fields = ("id", "name", "username", "password")

    name = fields.String(required=False)
    username = fields.String(required=True)
    password = fields.String(required=True)

