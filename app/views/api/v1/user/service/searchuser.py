from flask import Blueprint, request, abort, jsonify
from flask_restful import Api
from flasgger import swag_from

from app.views.api.v1.docs import SEARCH_USER_POST
from app.views import BaseResource
from app.models.user import UserModel
from app.models.question import QuestionModel

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/service/search_user')
class UserSearchManagement(BaseResource):
    @swag_from(SEARCH_USER_POST)
    def post(self):
        '''
        유저 검색
        '''
        search_user = request.json['search_id']

        user = UserModel.objects(id=search_user).first()

        if user is None:
            abort(406)

        QList = QuestionModel.objects(user=search_user).all()

        uuid_name_List = []
        a = 0

        for q in QList:
            uuid_name_List.append((q['uuid'], q['name']))

        Return_Str = str(
            {
                'user': {
                    'id': user['id'],
                    'name': user['name'],
                }
            },
        )

        Return_Str = Return_Str + str(' workbook : ')

        while True:
            if not uuid_name_List:
                break
            else:
                Return_Str = Return_Str + str(
                    {
                        a : {
                            'name': uuid_name_List[0][1],
                            'uuid': uuid_name_List[0][0],
                        },
                    }
                )
            del uuid_name_List[0]
            a += 1

        return jsonify(Return_Str)
