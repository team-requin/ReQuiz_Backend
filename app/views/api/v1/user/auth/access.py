from flask import Blueprint, abort
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from app.views import BaseResource
from app.views.api.v1.docs import ACCESS_POST

from app.models.user import UserModel

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/auth/token-access')
class TokenCheckManagement(BaseResource):
    @jwt_required
    @swag_from(ACCESS_POST)
    def post(self):
        '''
            유저 로그인 인증
        '''
        user_identity = get_jwt_identity()
        print(user_identity)

        user = UserModel.objects(id=user_identity).first()

        if user is None:
            abort(406)

        return {
            'user_id': user['id'],
            'user_name': user['name'],
            'user_level': user['level'],
            'user_exp': user['exp'],
        }, 201