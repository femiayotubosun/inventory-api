from application.extensions import ma
from marshmallow import validates_schema, validate, ValidationError


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
