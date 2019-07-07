from flask import Blueprint, request, abort
from flask_restful import Api
from flasgger import swag_from

from app.views.api.v1.docs import SEARCH_USER_POST
from app.views import BaseResource
from app.models.user import UserModel
from app.models.question import QuestionModel

blueprint = Blueprint(__name__,__name__)
api = Api(blueprint)

@api.resource('/service/searchuser')
class UserSearchManagement(BaseResource):
    def hello(self):
        return 'hello'

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


        for q in QList:
            uuid_name_List.append((q['uuid'], q['name']))

        while 1:
            if q is not None:


        return {
            'user': {
                'id': user['id'],
                'name': user['name'],
            },
                'workbook': {
                '1': {
                    'name': uuid_name_List[0][1],
                    'uuid': uuid_name_List[0][0],
                },
            }
        } if q is not None else {
            'WTF':'WTWTF!'
        }


        # def mk_json():
        #     return 'hello'
        #
        # return mk_json()

        # return {
        #     'user': {
        #         'id': user['id'],
        #         'name': user['name'],
        #     },
        #     'workbook': {
        #         '1': {
        #             'name': uuid_name_List[0][1],
        #             'uuid': uuid_name_List[0][0],
        #         },
        #         '2': {
        #             'name': uuid_name_List[1][1],
        #             'uuid': uuid_name_List[1][0],
        #         }
        #     }
        # }
