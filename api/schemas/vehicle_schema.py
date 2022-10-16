from api import ma
from ..models import vehicle_model
from marshmallow import fields


class VehicleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = vehicle_model.Vehicle
        load_instance = True
        fields = ("id", "model", "collor", "person")

    model = fields.String(required=True)
    collor = fields.String(required=True)
    person = fields.String(required=True)
