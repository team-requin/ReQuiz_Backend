from flask import Blueprint, request, abort
from flask_restful import Api

from app.views import BaseResource
from app.models.user import UserModel

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/service/searchuser')
class UserSearchManagement(BaseResource):
    '''
    유저 검색
    '''
    def post(self):
        search_user = request.json['search_id']

        user = UserModel.objects(id=search_user).first()

        if user is None:
            abort(406)

        return '', 201