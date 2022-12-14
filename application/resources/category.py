from flask import request
from flask_restful import Resource
from application.schemas import CategorySchema, ProductSchema
from application.services import CategoryService
from application.common.responses import (
    generic_success_response,
    create_resource_success_response,
    delete_resource_success_response,
)


class CategoryList(Resource):
    """
    Handles requests to '/categories/
    """

    def __init__(self, *args, **kwargs) -> None:
        self.category_service = kwargs["category_service"]

    def get(self):
        categories = self.category_service.find_categories()
        data = CategorySchema(many=True).dump(categories)
        return generic_success_response("All categories", data)

    def post(self):
        CategorySchema().load(request.json)
        self.category_service.create_category(**request.json)
        return create_resource_success_response("Category Created"), 201


class CategoryResource(Resource):
    """
    Handles request to '/categories/:category_id/
    """

    def __init__(self, *args, **kwargs):
        self.category_service = kwargs["category_service"]

    def get(self, category_id):
        category = self.category_service.find_category_by_id(category_id)
        data = CategorySchema().dump(category)
        return generic_success_response("Category details", data)

    def delete(self, category_id):
        self.category_service.delete_category(category_id)
        return None, 204

    def put(self, category_id):
        CategorySchema().load(request.json)
        self.category_service.update_category(category_id, **request.json)
        return generic_success_response("Category Updated")


class CategoryProductResource(Resource):
    def __init__(self, *args, **kwargs) -> None:
        self.category_service: CategoryService = kwargs["category_service"]

    def post(self, category_id):
        ProductSchema().load(request.json)
        self.category_service.create_product_for_category(category_id, **request.json)

        return create_resource_success_response("Product created for category"), 201
