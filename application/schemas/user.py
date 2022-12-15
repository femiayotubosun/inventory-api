from application.models import User
from application.extensions import ma, db


class UserSchema(ma.SQLAlchemyAutoSchema):
    id 