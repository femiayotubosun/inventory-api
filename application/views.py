from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from application.resources import ProductResource
from application.services import ProductService

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


product_service = ProductService()
api.add_resource(ProductResource, '/products/<int:product_id>/', endpoint="product_by_id", resource_class_kwargs={
'product_service': product_service
})


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e: ValidationError):
    """
    :param e: marshmallow validation error object
    :return: json error for marshmallow validation error

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400