from flask import Blueprint, request, abort
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource
from app.views.api.v1.docs import CHECK_ACCOUNT_POST

from app.models.user import UserModel

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/auth/sameaccount')
class CheckAccountManagement(BaseResource):
    @swag_from(CHECK_ACCOUNT_POST)
    def post(self):
        '''
        회원 가입시 중복 ID 확인
        '''
        id = request.json['id']

        check = UserModel.objects(id=id).first()

        if check is not None:
            abort(406)

        return '', 201