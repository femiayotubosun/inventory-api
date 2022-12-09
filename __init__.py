import os

from flask import Flask
from .common.database import db

#
# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     # app.config.from_mapping(
#     #     SECRET_KEY='dev',
#     #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     # )
#
#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#         print('Loading this')
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)
#
#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass
#
#     # a simple page that says hello
#
#     # attach blueprint
#
#     # attach_blueprints(app)
#     #
#     #
#     # connect_database(app)
#
#     return app


class Application:
    def __init__(self, test_config=None):
        self.app = Flask(__name__, instance_relative_config=True)

        # app.config.from_mapping(
        #     SECRET_KEY='dev',
        #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        # )

        if test_config is None:
            # load the instance config, if it exists, when not testing
            self.app.config.from_pyfile('config.py', silent=True)
            print('Loading this')
        else:
            # load the test config if passed in
            self.app.config.from_mapping(test_config)

    def attach_blueprints(self):
        pass

    def attach_extensions(self):
        db.init_app(self.app)

    def initialize_database(self):
        pass


app = Application().app

