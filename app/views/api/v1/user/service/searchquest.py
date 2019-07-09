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

        print(Quest['question'][0]['WAHT OS THIS'])

        if Quest is None:
            abort(406)

        #
        # for q in Quse:
        #     uuid_name_List.append((q['uuid'], q['name']))
        #
        # {
        #     0: {
        #         'q': 'a1',
        #         'a': 'a2'
        #     }
        # }

        # Str = {
        #     'Question_list': {
        #     },
        # }
        #
        # append_Str = {
        #     'Question_list': {
        #         'q': Quest[{['q']}],
        #         'a': user['name']
        #     },
        # }
        #
        # while True:
        #     if not uuid_name_List:
        #         break
        #
        #     else:
        #         append_Dict[Num] = {'name': uuid_name_List[0][1], 'uuid': uuid_name_List[0][0]}
        #
        #     del uuid_name_List[0]
        #     Num += 1
        #
        # Str['workbook'] = dict(append_Dict)
        #
        # return jsonify(Str)
