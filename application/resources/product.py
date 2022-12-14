from flask import request
from flask_restful import Resource
from application.services import ProductService
from application.schemas import ProductSchema


class ProductResource(Resource):
    def __init__(self, *args, **kwargs) -> None:
        self.product_service: ProductService = kwargs["product_service"]

    def get(self, product_id):
        product = self.product_service.find_product_by_id(product_id)
        return {"product": ProductSchema().dump(product)}


class ProductList(Resource):
    def __init__(self, *args, **kwargs) -> None:
        self.product_service = kwargs["product_service"]

    def get(self):
        products = self.product_service.find_products()
        return {"result": ProductSchema(many=True).dump(products)}

    def post(self):
        ProductSchema().load(request.json)
        self.product_service.create_product(**request.json)
        return {"result": "Success"}
