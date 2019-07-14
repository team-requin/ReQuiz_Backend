from flask import Blueprint, request, abort
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.views import BaseResource
from app.models.user import UserModel
from app.models.question import QuestionModel

blueprint = Blueprint(__name__,__name__)

api = Api(blueprint)

@api.resource('/service/delete-list')
class DeleteQuestionManagement(BaseResource):
    @jwt_required
    def post(self):
        user_id = get_jwt_identity()

        uuid = request.json['uuid']

        user = UserModel.objects(id = user_id).first()

        if user is None:
            abort(406)

        quest_uuid = QuestionModel.objects(uuid=uuid).first()

        if not quest_uuid['name'] == user_id:
            abort(409)

        pass