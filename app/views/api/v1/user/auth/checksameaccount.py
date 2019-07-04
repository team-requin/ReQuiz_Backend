from flask import Blueprint, request, abort
from flask_restful import Api

from app.models.user import UserModel
from app.views import BaseResource

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/auth/sameaccount')
class CheckAccountManagement(BaseResource):
    def post(self):
        id = request.json['id']

        check = UserModel.objects(id=id).first()

        if check is not None:
            abort(406)

        return '', 201