from flask import Blueprint, request, abort
from flask_restful import Api
from flasgger import swag_from

from app.views.api.v1.docs import UPDATE_Q_POST
from app.views import BaseResource
from app.models.question import QuestionModel

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/service/update-list')
class updateQListManagement(BaseResource):
    @swag_from(UPDATE_Q_POST)
    def post(self):
        '''
        문제 업데이트
        '''
        uuid = request.json['uuid']
        question = request.json['question']
        answer = request.json['answer']

        model = QuestionModel.objects(uuid=uuid).get()

        if model is None:
            abort(406)

        a = {
                'question':question,
                'answer':answer,
            },


        model.question.append(a)
        model.save()

        return '', 201