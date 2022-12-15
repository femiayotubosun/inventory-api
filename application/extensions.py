from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from passlib.context import CryptContext

db: SQLAlchemy = SQLAlchemy()
ma: Marshmallow = Marshmallow()
migrate: Migrate = Migrate()
jwt: JWTManager = JWTManager()
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

