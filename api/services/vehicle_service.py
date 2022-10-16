from ..models import vehicle_model
from api import db


def register_vehicle(vehicle):
    vehicle_bd = vehicle_model.Vehicle(
                model=vehicle.model,
                collor=vehicle.collor,
                person=vehicle.person,
            )
    db.session.add(vehicle_bd)
    db.session.commit()
    return vehicle_bd

def list_vehicles():
    vehicles = vehicle_model.Vehicle.query.all()
    return vehicles

def list_vehicle_by_id(id):
    vehicle = vehicle_model.Vehicle.query.filter_by(id=id).first()
    return vehicle

def update_vehicle(old_vehicle, new_vehicle):
    old_vehicle.model = new_vehicle.model
    old_vehicle.collor = new_vehicle.collor
    old_vehicle.person = new_vehicle.person
    db.session.commit()

def delete_vehicle(vehicle):
    db.session.delete(vehicle)
    db.session.commit()


