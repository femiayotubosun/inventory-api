from flask_restful import Resource
from flask import request
from application.schemas import SignupUserRequestSchema


class SignUpView(Resource):
    """
    This view handles signup requests
    """

    def post(self):
        SignupUserRequestSchema().load(request.json)
        return request.json
