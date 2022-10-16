from flask_restful import Resource
from api import api
from ..schemas import person_schema
from flask import request, make_response, jsonify
from ..entity import person
from ..services import person_service
from flask_jwt_extended import jwt_required, get_jwt
from ..decorator import admin_required


class PersonList(Resource):
    @jwt_required()
    def get(self):
        persons = person_service.list_persons()
        ps = person_schema.PersonSchema(many=True)
        return make_response(ps.jsonify(persons), 200)

    @jwt_required()
    def post(self):        
        ps = person_schema.PersonSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            new_person = person.Person(name=name)
            result = person_service.register_person(new_person)
            return make_response(ps.jsonify(result), 201)


class PersonDetail(Resource):
    @jwt_required()
    def get(self, id):
        person = person_service.list_person_by_id(id)
        if person is None:
            return make_response(jsonify("person não foi encontrado"), 404)
        ps = person_schema.PersonSchema()
        return make_response(ps.jsonify(person), 200)
    
    @admin_required
    def put(self, id):
        person_bd = person_service.list_person_by_id(id)
        if person_bd is None:
            return make_response(jsonify("person não foi encontrado"), 404)
        ps = person_schema.PersonSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            new_person = person.Person(name=name)
            person_service.update_person(person_bd, new_person)
            updated_person = person_service.list_person_by_id(id)
            return make_response(ps.jsonify(updated_person), 200)
    
    @admin_required
    def delete(self, id):
        person_bd = person_service.list_person_by_id(id)
        if person_bd is None:
            return make_response(jsonify("person não foi encontrado"), 404)
        person_service.delete_person(person_bd)
        return make_response("person excluido com sucesso", 204)

api.add_resource(PersonList, '/persons')
api.add_resource(PersonDetail, '/persons/<int:id>')
