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
            'name': 'TOKEN',
            'in': 'token',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'JUSTCHECK': '확인후 반환',
        }
    }
}


UPDATE_Q_POST = {
    'tags': ['Service'],
    'parameters': [
        {
            'name': 'Question , Answer',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'JUSTCHECK': '확인후 반환',
        }
    }
}


SEARCH_USER_POST = {
    'tags': ['Service'],
    'parameters': [
        {
            'name': 'Name',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'Any':'Types',
        }
    }
}
