from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db: SQLAlchemy = SQLAlchemy()
ma: Marshmallow = Marshmallow()
migrate = Migrate()
