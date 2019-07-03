from flask import Blueprint, abort
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.views import BaseResource
from app.models.user import UserModel

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/auth/token_access')
class TokenCheckManagement(BaseResource):
    '''
    유저 로그인 인증
    '''
    @jwt_required
    def get(self):
        user_identity = get_jwt_identity()

        user = UserModel.objects(id=user_identity).first()

        if user is None:
            abort(406)

        return {
            'username': user
        }