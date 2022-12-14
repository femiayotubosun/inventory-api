from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from application.common import APIError
from application.services import ProductService, CategoryService
from application.resources import (
    ProductResource,
    ProductList,
    CategoryList,
    CategoryResource,
    CategoryProductResource,
)

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)


# Product Endpoints

api.add_resource(
    ProductList,
    "/products/",
    endpoint="product_list",
    resource_class_kwargs={"product_service": ProductService},
)


api.add_resource(
    ProductResource,
    "/products/<int:product_id>/",
    endpoint="product_by_id",
    resource_class_kwargs={"product_service": ProductService},
)


# Category Endpoints

api.add_resource(
    CategoryList,
    "/categories/",
    endpoint="categories_list",
    resource_class_kwargs={"category_service": CategoryService},
)


api.add_resource(
    CategoryResource,
    "/categories/<int:category_id>/",
    endpoint="category_by_id",
    resource_class_kwargs={"category_service": CategoryService},
)

api.add_resource(
    CategoryProductResource,
    "/categories/<int:category_id>/products/",
    endpoint="create_product_in_category",
    resource_class_kwargs={"category_service": CategoryService},
)

# Error Handlers


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e: ValidationError):
    """
    :param e: marshmallow validation error
    :return: json error for marshmallow validation error

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400


@blueprint.errorhandler(APIError)
def handle_api_errors(e: APIError):
    """

    :param e: custom APIError error
    :return: json error for APIError

    This returns correct JSON response with associated
    HTTP 4xx Status as defined in the exceptions
    """

    return (
        jsonify(
            {
                "status": "error",
                "status_code": e.status_code,
                "message": e.message,
                "result": None,
            }
        ),
        e.status_code,
    )
