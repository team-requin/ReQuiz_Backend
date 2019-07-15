LOGIN_POST = {
    'tags': ['Auth'],
    'description': '로그인',
    'parameters': [
        {
            'name': 'id',
            'description': 'ID',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'pw',
            'description': 'PASSWORD',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
            '201': {
                'description': '로그인 성공',
                'examples': {
                    '': {
                        'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.T26Dm4buOBRdxNs58srk1l_N5y1Dxii9y-YMj-9J7mM',
                        'refreshToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.T26Dm4buOBRdxNs58srk1l_N5y1Dxii9y-YMj-9J7mM'
                    }
                }
            },
            '406': {
                'description': '로그인 실패'
            }
        }
}


REGISTER_POST = {
    'tags': ['Auth'],
    'description': '회원가입',
    'parameters': [
        {
            'name': 'id',
            'description': 'ID',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'pw',
            'description': 'PASSWORD',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw_check',
            'description': 'CHECK THE PASSWORD',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'name',
            'description': 'USER NAME',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '회원가입 성공',
        },
        '406': {
            'description': '패스워드와 패스워드 확인이 다름'
        },
        '409': {
            'description': '이미 존재하는 아이디'
        }
    }
}


ACCESS_POST = {
    'tags': ['Auth'],
    'parameters': [
        {
            'name': 'Bearer token',
            'description': 'JWT',
            'in': 'JWT',
            'type': 'str',
            'required': True,
        },
    ],
    'responses': {
        '201': {
                'description': '인증 성공',
                'examples': {
                    '': {
                        'user_id': 'admin',
                        'user_name': 'ADMIN',
                        'user_level': 3,
                        'user_exp': 30,
                    }
                }
            },
        '406': {
            'description': '존재하지 않는 아이디',
        }
    }
}


CHECK_ACCOUNT_POST = {
    'tags': ['Auth'],
    'parameters': [
        {
            'name': 'id',
            'description': '확인할 사용자 ID',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
    ],
    'responses': {
        '201': {
            'description': '등록 되지 않은 ID',
            },
        '406': {
            'description': '이미 등록된 ID',
        }
    }
}


CHECK_NAME_POST = {
    'tags': ['Auth'],
    'parameters': [
        {
            'name': 'name',
            'description': '확인할 사용자 이름',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
    ],
    'responses': {
        '201': {
                'description': '등록 되지 않은 닉네임',
            },
        '406': {
            'description': '이미 등록된 닉네임',
        }
    }
}


CREATE_Q_POST = {
    'tags': ['Service'],
    'parameters': [
        {
            'name': 'Bearer token',
            'description': 'JWT',
            'in': 'JWT',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'quest_name',
            'description': '만들 문제 이름',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
    ],
    'responses': {
        '201': {
            'description': '문제 생성 성공',
        },
        '406': {
            'description': '존재하지 않는 아이디',
        },
    }
}


UPDATE_Q_POST = {
    'tags': ['Service'],
    'parameters': [
        {
            'name': 'uuid',
            'description': '문제의 uuid',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'question',
            'description': '만들 문제 질문',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'answer',
            'description': '만들 문제 답',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
    ],
    'responses': {
        '201': {
            'description': '문제 업데이트 성공',
        }
    }
}


SEARCH_USER_POST = {
    'tags': ['Service'],
    'parameters': [
        {
            'name': 'search_id',
            'description': '검색할 유저 ID',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
    ],
    'responses': {
        '201': {
            'description': '검색 성공',
            'examples': {
                "user": {
                    "id": "admin",
                    "name": "Admin"
                },
                "workbook": {
                    "0": {
                        "name": "test1",
                        "uuid": "12668"
                    },
                    "1": {
                        "name": "test2",
                        "uuid": "45130"
                    },
                    "2": {
                        "name": "test3",
                        "uuid": "51529"
                    },
                    "3": {
                        "name": "test3",
                        "uuid": "30106"
                    }
                }
            }
        },
        '406': {
            'description': '존재하지 않는 유저',
        }
    }
}

SEARCH_Q_POST = {
    'tags': ['Service'],
    'parameters': [
        {
            'name': 'uuid',
            'description': '검색할 UUID',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
    ],
    'responses': {
        '200': {
            'description': '검색 성공',
            'examples': {
                "list": {
                    "0": {
                        "answer": "Atest1",
                        "question": "Qtest1"
                    },
                    "1": {
                        "answer": "Atest2",
                        "question": "Qtest2"
                    },
                    "2": {
                        "answer": "Atest3",
                        "question": "Qtest3"
                     }
                 },
                "title": "TESTTITLE"
            }
        },
        '406': {
            'description': '존재하지 않는 uuid',
        }
    }
}

CREATE_RE_Q_POST = {
    'tags': ['Service'],
    'parameters': [
        {
            'name': 'uuid',
            'description': '접근할 uuid 만약 없을시 새로 생성',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'title',
            'description': '만들 문제의 제목',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'list',
            'description': '수정하거나 만들 문제',
            'in': 'json',
            'type': 'str',
            'required': True,
        },
    ],
    'responses': {
        '201': {
            'description': '문제 생성 또는 업데이트 성공',
            'examples': {
                "uuid": "12345"
            }
        },
        '406': {
            'description': '존재하지 않는 유저',
        }
    }
}