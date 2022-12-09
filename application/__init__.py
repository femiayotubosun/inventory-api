from flask import Flask
from application.extensions import db, migrate
from application.views import blueprint as app_bp


class Application:
    def __init__(self, test_config=None):
        self.app = Flask(__name__, instance_relative_config=True)
        if test_config is None:
            self.app.config.from_object("application.config")
        else:
            self.app.config.from_mapping(test_config)

        self.configure_extensions()
        self.register_blueprints()

    def register_blueprints(self):
        self.app.register_blueprint(app_bp)

    def configure_extensions(self):
        db.init_app(self.app)
        migrate.init_app(self.app, db)



