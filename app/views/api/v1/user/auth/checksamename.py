from flask import Blueprint, request, abort
from flask_restful import Api

from app.models.user import UserModel
from app.views import BaseResource

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)


@api.resource('/auth/samename')
class CheckAccountNameManagement(BaseResource):
    def post(self):
        name = request.json['name']

        check = UserModel.objects(name=name).first()

        if check is not None:
            abort(406)

        return '', 201