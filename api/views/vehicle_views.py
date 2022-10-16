from flask_restful import Resource
from api import api
from ..schemas import vehicle_schema
from flask import request, make_response, jsonify
from ..entity import vehicle
from ..services import vehicle_service, person_service
from flask_jwt_extended import jwt_required


class VehicleList(Resource):
    @jwt_required()
    def get(self):
        vehicle = vehicle_service.list_vehicles()
        vs = vehicle_schema.VehicleSchema(many=True)
        return make_response(vs.jsonify(vehicle), 200)

    @jwt_required()
    def post(self):
        vs = vehicle_schema.VehicleSchema()
        validate = vs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            model = request.json["model"]
            collor = request.json["collor"]
            person = request.json["person"]
            person_vehicle = person_service.list_person_by_id(person)
            if person_vehicle is None:
                return make_response(jsonify("vehicle not found"), 404)

            new_vehicle = vehicle.Vehicle(model=model,
                                     collor=collor,
                                     person=person_vehicle)
            result = vehicle_service.register_vehicle(new_vehicle)
            return make_response(vs.jsonify(result), 201)


class VehicleDetail(Resource):
    @jwt_required()
    def get(self, id):
        vehicle = vehicle_service.list_vehicle_by_id(id)
        if vehicle is None:
            return make_response(jsonify("vehicle not found"), 404)
        vs = vehicle_schema.VehicleSchema()
        return make_response(vs.jsonify(vehicle), 200)

    @jwt_required()
    def put(self, id):
        vehicle_bd = vehicle_service.list_vehicle_by_id(id)
        if vehicle_bd is None:
            return make_response(jsonify("vehicle not found"), 404)
        vs = vehicle_schema.VehicleSchema()
        validate = vs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            model = request.json["model"]
            collor = request.json["collor"]
            person = request.json["person"]
            person_vehicle = person_service.listar_person_id(person)
            if person_vehicle is None:
                return make_response(jsonify("vehicle not found"), 404)

            new_vehicle = vehicle.Vehicle(model=model,
                                     collor=collor,
                                     person=person_vehicle)

            vehicle_service.update_vehicle(vehicle_bd, new_vehicle)
            updated_vehicle = vehicle_service.list_vehicle_by_id(id)
            return make_response(vs.jsonify(updated_vehicle), 201)
    
    @jwt_required()
    def delete(self, id):
        vehicle_bd = vehicle_service.list_vehicle_by_id(id)
        if vehicle_bd is None:
            return make_response(jsonify("vehicle not found"), 404)
        vehicle_service.delete_vehicle(vehicle_bd)
        return make_response("vehicle excluido com sucesso", 204)

api.add_resource(VehicleList, '/vehicle')
api.add_resource(VehicleDetail, '/vehicle/<int:id>')