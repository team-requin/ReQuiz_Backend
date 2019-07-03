from flask import Blueprint, request, abort
from flask_restful import Api
from app.views import BaseResource
from app.models.user import UserModel

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/auth/register')
class RegisterManagement(BaseResource):
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

        if UserModel.objects(id=id).first():
            abort(406)

        UserModel(
            id = id,
            pw = pw,
            name = name,
        ).save()

        return '', 201