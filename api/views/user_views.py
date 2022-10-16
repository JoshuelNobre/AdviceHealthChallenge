from flask_restful import Resource
from api import api
from ..schemas import user_schema
from flask import request, make_response, jsonify
from ..entity import user
from ..services import user_service


class UserList(Resource):

    def post(self):
        us = user_schema.UserSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            username = request.json["username"]
            password = request.json["password"]
            is_admin = request.json["is_admin"]

            new_user = user.User(name=name, username=username, password=password, is_admin=is_admin)
            resultado = user_service.register_users(new_user)
            return make_response(us.jsonify(resultado), 201)


api.add_resource(UserList, '/user')

