from flask import Blueprint, request, abort
from flask_restful import Api
from flask_jwt_extended import create_access_token, create_refresh_token
from flasgger import swag_from

from app.views import BaseResource
from app.models.user import UserModel
from app.views.api.v1.docs import LOGIN_POST

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/auth/login')
class LoginManagement(BaseResource):
    @swag_from(LOGIN_POST)
    def post(self):
        '''
        유저 로그인
        '''
        id = request.json['id']
        pw = request.json['pw']

        user = UserModel.objects(id=id, pw=pw).first()

        if user is None:
            abort(406)

        return {
            'access_token': create_access_token(identity=id),
            'refresh_token': create_refresh_token(identity=id),
        }