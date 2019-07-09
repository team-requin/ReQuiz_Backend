from flask import Blueprint, request, abort, jsonify
from flask_restful import Api
from flasgger import swag_from

from app.views.api.v1.docs import SEARCH_USER_POST
from app.views import BaseResource
from app.models.user import UserModel
from app.models.question import QuestionModel

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/service/search-user')
class UserSearchManagement(BaseResource):
    @swag_from(SEARCH_USER_POST)
    def post(self):
        '''
        유저 검색
        '''
        Num = 0
        append_Dict = dict()
        uuid_name_List = list()
        search_user = request.json['search_id']
        user = UserModel.objects(id=search_user).first()
        QList = QuestionModel.objects(user=search_user).all()

        if user is None:
            abort(406)

        for q in QList:
            uuid_name_List.append((q['uuid'], q['name']))

        Str = {
            'user': {
                'id': user['id'],
                'name': user['name']
            },
            'workbook' : {
            }
        }

        while True:
            if not uuid_name_List:
                break

            else:
                append_Dict[Num] = {'name': uuid_name_List[0][1], 'uuid': uuid_name_List[0][0]}

            del uuid_name_List[0]
            Num += 1

        Str['workbook'] = dict(append_Dict)

        return jsonify(Str)
