from flask import Flask
from mongoengine import *
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app.views import Router

def create_app(*config_cls):
    flask_app = Flask(__name__)

    for config in config_cls:
        flask_app.config.from_object(config)

    connect(**flask_app.config['MONGODB_SETTINGS'])

    CORS(flask_app, resources={
        r"*": {"origin": "*"},
    })

    JWTManager().init_app(flask_app)
    Router().init_app(flask_app)

    return flask_app