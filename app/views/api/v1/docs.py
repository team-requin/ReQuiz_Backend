LOGIN_POST = {
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
            'description': 'token',
        }
    }
}

REGISTER_POST = {
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
                'description': '로그인 가능한 ID 및 PW',
            }
        }
    }