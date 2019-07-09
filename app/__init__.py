from flask import Flask
from mongoengine import *
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger

from app.misc.log import log
from app.views import Router
from config import Config

def create_app(*config_cls):

    log(message='Flask application initialized with {}'.format(', '.join([config.__name__ for config in config_cls])),
        keyword='INFO')

    flask_app = Flask(__name__)

    for config in config_cls:
        flask_app.config.from_object(config)

    connect(**flask_app.config['MONGODB_SETTINGS'])

    CORS(flask_app, resources={
        r"*": {"origin": "*"},
    })

    swagger = Swagger(template=Config.template)
    swagger.init_app(flask_app)

    JWTManager().init_app(flask_app)
    Router().init_app(flask_app)

    return flask_app