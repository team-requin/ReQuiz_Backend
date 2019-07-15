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

        from app.views.api.v1.user.auth import checksameaccount, checksamename,edituser
        app.register_blueprint(checksamename.api.blueprint)
        app.register_blueprint(checksameaccount.api.blueprint)
        app.register_blueprint(edituser.api.blueprint)

        from app.views.api.v1.user.service import searchuser, searchquest,re_create_list
        # app.register_blueprint(createlist.api.blueprint)
        # app.register_blueprint(updatelist.api.blueprint)
        app.register_blueprint(searchuser.api.blueprint)
        app.register_blueprint(searchquest.api.blueprint)
        app.register_blueprint(re_create_list.api.blueprint)
