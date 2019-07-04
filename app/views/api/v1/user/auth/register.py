from flask import Blueprint, request, abort
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource
from app.models.user import UserModel
from app.views.api.v1.docs import REGISTER_POST

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/auth/register')
class RegisterManagement(BaseResource):
    @swag_from(REGISTER_POST)
    def post(self):
        '''
        유저 회원가입
        '''
        id = request.json['id']
        pw = request.json['pw']
        pw_check = request.json['pw_check']
        name = request.json['name']

        if not pw == pw_check:
            abort(406)

        user = UserModel.objects(id=id).first()

        if user is not None:
            abort(409)

        UserModel(
            id = id,
            pw = pw,
            name = name,
        ).save()

        return '', 201