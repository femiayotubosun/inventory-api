from application.extensions import ma, db
from application.models import User
from marshmallow import validates_schema, validate, ValidationError


class UserSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)
    password = ma.String(load_only=True, required=True)

    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True
        exclude = ("_password",)


class SignupUserRequestSchema(ma.Schema):
    email = ma.Email(required=True)
    password = ma.String(validate=validate.Length(min=7), required=True)
    password_confirm = ma.String(required=True)

    @validates_schema
    def validate_password_confirm(self, data, **kwargs):
        if data["password"] != data["password_confirm"]:
            raise ValidationError(
                "password_confirm must match password", field_name="password_confirm"
            )


class SignInUserRequestSchema(ma.Schema):
    email = ma.Email(required=True)
    password = ma.String(required=True)
