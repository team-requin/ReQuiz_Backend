from flask import Blueprint, request, abort
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource
from app.views.api.v1.docs import CHECK_NAME_POST

from app.models.user import UserModel


blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/auth/check-same-name')
class CheckAccountNameManagement(BaseResource):
    @swag_from(CHECK_NAME_POST)
    def post(self):
        '''
        회원 가입시 중복 Name 확인
        '''
        name = request.json['name']

        check = UserModel.objects(name=name).first()

        if check is not None:
            abort(406)

        return '', 201