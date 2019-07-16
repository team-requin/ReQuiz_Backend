from flask import Blueprint, abort, request
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from app.views.api.v1.docs import CREATE_Q_POST
from app.views import BaseResource
from app.models.user import UserModel
from app.models.question import QuestionModel

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/service/create-list')
class CreateListManagement(BaseResource):
    @jwt_required
    @swag_from(CREATE_Q_POST)
    def post(self):
        '''
        문제 테이블 생성 및 수정
        '''
        user_identity = get_jwt_identity()

        quest_uuid = request.json['uuid']
        quest_name = request.json['title']
        quest_list = request.json['list']

        find = QuestionModel.objects(uuid=quest_uuid).first()

        user = UserModel.objects(id=user_identity).first()

        if user is None:
            abort(406)


        if find is None:
            quest = {}

            for a in quest_list:
                quest[a] = {
                    'question': quest_list[str(a)]['q'],
                    'answer': quest_list[str(a)]['a']
                }

            QuestionModel(
                gar = quest_uuid,
                uuid = quest_uuid,
                name = quest_name,
                user = user_identity,
                question = quest,
            ).save()

        else:
            quest = {}

            for a in quest_list:
                quest[a] = {
                    'question': quest_list[str(a)]['q'],
                    'answer': quest_list[str(a)]['a']
                }

            find.update(question=quest)


        return {
            'uuid': quest_uuid
               }, 201