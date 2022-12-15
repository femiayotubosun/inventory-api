from application.extensions import db
from application.schemas import UserSchema


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
        # GET USER CREDENTIALS
        
        # Check if User Exists
        
        # Check if password matches
        
        # send token
