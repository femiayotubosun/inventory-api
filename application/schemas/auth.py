from application.extensions import ma, db


class SignupUserRequestSchema(ma.Schema):
    email = ma.Email(required=True)
    password = ma.String(min=7, required=True)
    password_confirm = ma.String(required=True)

    @ma.validate("password_confirm")
    def validate_password_confirm(self, obj, value):
        if obj.password != value:
            raise ma.ValidationError("password_confirm must match password")
