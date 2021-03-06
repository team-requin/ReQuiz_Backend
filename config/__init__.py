class Config:
    SERVICE_NAME = 'ReQUIZ'

    _LOCALHOST = '127.0.0.1'

    HOST = '0.0.0.0'
    PORT = 80
    DEBUG = True

    MONGO_HOST = _LOCALHOST
    MONGO_PORT = ''
    MONGO_ID = ''
    MONGO_PW = ''

    SECRET_KEY = 'THISISSECRETKEY'

    RUN_SETTINGS = {
        'host': HOST,
        'port': PORT,
        'debug': DEBUG,
    }

    MONGODB_SETTINGS = {
        'db': SERVICE_NAME,
        'host': MONGO_HOST,
        'port': MONGO_PORT,
        'username': MONGO_ID,
        'password': MONGO_PW,
    }

    SWAGGER = {
        'title': 'DOCS',
        'specs_route': '/swaggerdocs',
        'uiversion': 3,

        'info': {
            'title': 'Requiz docs',
            'version': 'Beta',
            'description': ''
        },

        'host': 'ec2-15-164-169-0.ap-northeast-2.compute.amazonaws.com',
        'basePath': '/ '
    }

    template = {
        'schemes': [
            'http'
        ]
    }
