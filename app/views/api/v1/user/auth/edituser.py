from flask import Blueprint, request, abort
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.user import UserModel
from app.views import BaseResource

blueprint = Blueprint(__name__,__name__)

api = Api(blueprint)

@api.resource('/auth/user-edit')
class UserEditManagement(BaseResource):
    @jwt_required
    def post(self):
        name = request.json['name']
        pw = request.json['pw']
        pw_chk = request.json['pw_check']

        access_user = get_jwt_identity()

        user = UserModel.objects(id=access_user).first()

        if not pw == pw_chk:
            abort(409)

        user.update(name=name,pw = pw,)

        return '',201