from flask import Blueprint, abort, request
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.views import BaseResource
from app.models.user import UserModel
from app.models.question import QuestionModel

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/service/createlist')
class CreateListManagement(BaseResource):
    @jwt_required
    def post(self):
        user_identity = get_jwt_identity()

        user = UserModel.objects(id=user_identity).first()

        if user is None:
            abort(406)

        question = request.json['question']

        QuestionModel(
            id = user,
            question = question,
        ).save()

        return '', 201