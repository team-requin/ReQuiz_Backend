from flask import Blueprint, request, abort, jsonify
from flask_restful import Api

from app.models.user import UserModel
from app.models.question import QuestionModel
from app.views import BaseResource

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/service/search-question')
class SearchUserManagement(BaseResource):
    def get(self):
        uuid = request.json['uuid']
        Quest = QuestionModel.objects(uuid=uuid).first()
        Num = 0
        append_Dict = dict()
        QNA_LIST = list()

        if Quest is None:
            abort(406)

        for q in Quest:
            print(Quest['question'][q][0]['question'])
            print(Quest['question'][q][0]['answer'])
            QNA_LIST.append((Quest['question'][q][0]['question'],
                             Quest['question'][q][0]['answer']))

        Str = {
            'Question_list': {
            },
        }

        while True:
            if not QNA_LIST:
                break

            else:
                append_Dict[Num] = {'question': QNA_LIST[0][0], 'answer': QNA_LIST[0][1]}

            del QNA_LIST[0]
            Num += 1

        Str['Question_list'] = dict(append_Dict)

        print(Str)

        return jsonify(Str)
