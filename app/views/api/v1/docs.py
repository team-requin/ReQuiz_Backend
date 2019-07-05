LOGIN_POST = {
    'tags': ['Auth'],
    'parameters': [
        {
            'name': 'id, pw',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': 'token',
        }
    }
}


REGISTER_POST = {
        'tags': ['Auth'],
        'parameters': [
            {
                'name': 'id, pw, pw_check, name',
                'in': 'json',
                'type': 'str',
                'required': True
            }
        ],
        'responses': {
            '201': {
                'description': '로그인 가능한 ID 및 PW',
            }
        }
    }


ACCESS_POST = {
    'tags': ['Auth'],
    'parameters': [
        {
            'name': 'token',
            'in': 'token',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': 'name',
        }
    }
}


CHECK_ACCOUNT_POST = {
    'tags': ['Auth'],
    'parameters': [
        {
            'name': 'id',
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


CHECK_NAME_POST = {
    'tags': ['Auth'],
    'parameters': [
        {
            'name': 'name',
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
