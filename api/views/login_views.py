from os import access
from flask_restful import Resource
from api import api, jwt
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..entity import user
from ..services import user_service
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta


class LoginList(Resource):

    @jwt.additional_claims_loader
    def add_claims_to_access_token(identity):
        user_token = user_service.list_user_id(identity)

        if user_token.is_admin:
            roles = 'admin'
        else:
            roles = 'user'
        return {'roles': roles}

    def post(self):
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            username = request.json["username"]
            password = request.json["password"]

            user_bd = user_service.list_user_username(username)
            
            if user_bd and user_bd.verify_password(password):
                access_token = create_access_token(
                    identity=user_bd.id,
                    expires_delta=timedelta(seconds=100)
                )
                refresh_token = create_refresh_token(
                    identity=user_bd.id
                )
                return make_response(jsonify({
                    'access_token': access_token,
                    'refresh_token': refresh_token,
                    'message': 'Login realizado com sucesso'
                }))

            return make_response(jsonify({
                'message': 'Crendicias estãoo invalidas'
            }, 401))


api.add_resource(LoginList, '/login')

