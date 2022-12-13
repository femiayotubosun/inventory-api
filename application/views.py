from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from application.common import APIError
from application.services import ProductService
from application.resources import ProductResource, ProductList

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(
    ProductResource,
    "/products/<int:product_id>/",
    endpoint="product_by_id",
    resource_class_kwargs={"product_service": ProductService},
)

api.add_resource(
    ProductList,
    "/products",
    endpoint="product_list",
    resource_class_kwargs={"product_service": ProductService},
)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e: ValidationError):
    """
    :param e: marshmallow validation error
    :return: json error for marshmallow validation error

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400


# @blueprint.errorhandler(APIError)
# def handle_api_errors(e: APIError):
#     """

#     :param e: custom APIError error
#     :return: json error for APIError

#     This will avoid having to try/catch Errors in all endpoints, returning
#     correct JSON response with associated HTTP 4xx Status as defined the exceptions
#     """

#     return jsonify(e.),
