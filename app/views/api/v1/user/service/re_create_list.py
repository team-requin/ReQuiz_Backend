from flask import Blueprint, abort, request
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from
import random

from app.views.api.v1.docs import CREATE_Q_POST
from app.views import BaseResource
from app.models.user import UserModel
from app.models.question import QuestionModel

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/service/re-create-list')
class CreateListManagement(BaseResource):
    # @jwt_required
    def post(self):
        '''
        문제 테이블 생성
        '''

        test = request.json['title']
        list = request.json['list']

        print(test)
        print(list['0']["asdasdasdasd"])

        # user_identity = get_jwt_identity()
        #
        # quest_name = request.json['title']
        # quest_list = request.json['list']
        #
        # print(quest_name)
        # print(quest_list)

        # user = UserModel.objects(id=user_identity).first()
        #
        # if user is None:
        #     abort(406)
        #
        # while True:
        #     uuid = str(random.randrange(11111,99999))
        #/
        #     check_uuid = QuestionModel.objects(uuid=uuid).first()
        #
        #     if check_uuid is None:
        #         break
        #
        # print(uuid)
        #
        # QuestionModel(
        #     gar = uuid,
        #     uuid = uuid,
        #     name = quest_name,
        #     user = user_identity,
        #     question = None,
        # ).save()
        #
        # return '', 201