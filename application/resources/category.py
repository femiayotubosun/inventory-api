from flask import request
from flask_restful import Resource
from application.schemas import CategorySchema




class CategoryList(Resource):
    def __init__(self, *args, **kwargs) -> None:
        self.category_service = kwargs["category_service"]

    def get(self):
        categories = self.category_service.find_categories()
        return {
            "message": "All Categories",
            "status": "success",
            "status_code": "200",
            "result": CategorySchema(many=True).dump(categories),
        }

    def post(self):
        CategorySchema().load(request.json)
        self.category_service.create_category(**request.json)
        return {
            "message": "Category Created ",
            "status": "success",
            "status_code": "201",
            "result": None,
        }

class CategoryResource(Resource):
    def __init__(self, *args, **kwargs):
        self.category_service = kwargs["category_service"]

    def get(self, category_id):
        category = self.category_service.find_category_by_id(category_id)
        return {"category": CategorySchema().dump(category)}

    def delete(self, category_id):
        self.category_service.delete_category(category_id)
        return {
            "message": "Deleted Category",
            "status": "success",
            "status_code": "204",
            "result": None,
        }

    def put(self, category_id):
        CategorySchema().load(request.json)
        self.category_service.update_category(category_id, **request.json)
        return {"message": "success"}


