from flask_restful import Resource
from flask import request
from application.schemas import SignupUserRequestSchema
from application.services import AuthService
from application.common.responses import generic_success_response


class SignUpAction(Resource):
    """
    This view handles signup requests
    """

    def post(self):
        SignupUserRequestSchema().load(request.json)
        AuthService.signup_user(**request.json)
        return generic_success_response("Signup Successful")
