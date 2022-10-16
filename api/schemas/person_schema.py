from api import ma
from ..models import person_model
from marshmallow import fields
from ..schemas import vehicle_schema


class PersonSchema(ma.SQLAlchemySchema):
    class Meta:
        model = person_model.Person
        load_instance = True
        fields = ("id", "name", "vehicle")

    name = fields.String(required=True)
    vehicle = fields.List(fields.Nested(vehicle_schema.VehicleSchema, only=('model', 'collor')))


