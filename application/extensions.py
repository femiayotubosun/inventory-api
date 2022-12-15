from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from passlib.context import CryptContext


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

db: SQLAlchemy = SQLAlchemy(metadata=metadata)
ma: Marshmallow = Marshmallow()
migrate: Migrate = Migrate()
jwt: JWTManager = JWTManager()
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
