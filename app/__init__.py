from flask import Flask
from flask_restful import Api
import config


def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(config.app_config[config_name])

    with app.app_context():
        from . resources.user_resource import SignupResource, LoginResource
        from . resources.entry_resource import EntryResource

    api.add_resource(SignupResource, '/api/v1/user/signup')
    api.add_resource(LoginResource, '/api/v1/user/login')
    api.add_resource(EntryResource, '/api/v1/user/entries', '/api/v1/user/entries/<int:entry_id>')

    return app
