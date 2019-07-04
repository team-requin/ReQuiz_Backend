from flask_restful import Resource

class BaseResource(Resource):
    pass

class Router:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from app.views.api.v1.user.auth import register, login, access
        app.register_blueprint(register.api.blueprint)
        app.register_blueprint(login.api.blueprint)
        app.register_blueprint(access.api.blueprint)

        from app.views.api.v1.user.auth import checksameaccount, checksamename
        app.register_blueprint(checksamename.api.blueprint)
        app.register_blueprint(checksameaccount.api.blueprint)

        from app.views.api.v1.user.service import createlist, updatelist, searchuser
        app.register_blueprint(createlist.api.blueprint)
        app.register_blueprint(searchuser.api.blueprint)
        app.register_blueprint(updatelist.api.blueprint)
