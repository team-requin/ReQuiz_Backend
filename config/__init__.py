class LocalLevelConfig:
    SERVICE_NAME = 'ReQUIZ'

    _LOCALHOST = '127.0.0.1'

    HOST = '0.0.0.0'
    PORT = 80
    DEBUG = True

    MONGO_HOST = _LOCALHOST
    MONGO_PORT = ''
    MONGO_ID = ''
    MONGO_PW = ''

    SQL_HOST = _LOCALHOST
    SQL_PORT = ''
    SQL_ID = ''
    SQL_PW = ''

    SECRET_KEY = 'THISISSECRETKEY'

    RUN_SETTINGS = {
        'host': HOST,
        'port': PORT,
        'debug': DEBUG,
    }

    MONGO_DB_SETTINGS = {
        'db': SERVICE_NAME,
        'host': MONGO_HOST,
        'port': MONGO_PORT,
        'username': MONGO_ID,
        'password': MONGO_PW,
    }

