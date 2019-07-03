from flask import Flask
from app.views import Router
from mongoengine import *

def create_app(*config_cls):
    flask_app = Flask(__name__)

    for config in config_cls:
        flask_app.config.from_object(config)

    connect(**flask_app.config['MONGODB_SETTINGS'])
    Router().init_app(flask_app)

    return flask_app