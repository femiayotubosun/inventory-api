from flask_jwt_extended import create_access_token

from application.extensions import db, pwd_context
from application.schemas import UserSchema
from application.models import User
from application.common.exceptions import BadRequestError


class AuthService:
    @staticmethod
    def signup_user(**kwargs):
        del kwargs["password_confirm"]
        schema = UserSchema()
        user = schema.load(kwargs)

        db.session.add(user)
        db.session.commit()

    @staticmethod
    def signin_user(**kwargs):

        email = kwargs.get("email", None)
        password = kwargs.get("password", None)

        if email is None or password is None:
            raise BadRequestError("email or password is missing")

        user = User.query.filter_by(email=email).first()
        if user is None or not pwd_context.verify(password, user.password):
            raise BadRequestError("Bad credentials")

        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}
