from flask import Blueprint, request, abort, jsonify
from flask_restful import Api
from flasgger import swag_from

from app.views.api.v1.docs import SEARCH_Q_POST
from app.models.question import QuestionModel
from app.views import BaseResource

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)
# api.prefix('/service')

@api.resource('/service/search-question')
class SearchUserManagement(BaseResource):
    @swag_from(SEARCH_Q_POST)
    def post(self):
        '''
        질문 검색
        '''
        uuid = request.json['uuid']
        Quest = QuestionModel.objects(uuid=uuid).first()
        name = QuestionModel.objects(uuid=uuid).first()
        Num = 0
        append_Dict = dict()
        QNA_LIST = list()

        if Quest is None:
            abort(406)

        for q in Quest['question']:
            QNA_LIST.append((
                q[0]['question'],
                q[0]['answer']
            ))

        Str = {
            'name': str(name['name']),
            'list': {
            },
        }

        while True:
            if not QNA_LIST:
                break

            else:
                append_Dict[Num] = {'question': QNA_LIST[0][0], 'answer': QNA_LIST[0][1]}

            del QNA_LIST[0]
            Num += 1

        Str['list'] = dict(append_Dict)

        return jsonify(Str)
