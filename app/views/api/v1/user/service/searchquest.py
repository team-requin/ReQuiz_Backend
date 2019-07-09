from flask import Blueprint, request, abort, jsonify
from flask_restful import Api

from app.models.question import QuestionModel
from app.views import BaseResource

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/service/search-question')
class SearchUserManagement(BaseResource):
    def post(self):
        uuid = request.json['uuid']
        Quest = QuestionModel.objects(uuid=uuid).first()
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
