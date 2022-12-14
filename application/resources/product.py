from flask import request
from flask_restful import Resource
from application.services import ProductService
from application.schemas import ProductSchema
from application.common.responses import generic_success_response


class ProductList(Resource):
    """
    Hanles requests to '/products/
    """

    def __init__(self, *args, **kwargs) -> None:
        self.product_service = kwargs["product_service"]

    def get(self):
        products = self.product_service.find_products()
        data = ProductSchema(many=True).dump(products)
        return generic_success_response("All products", data)


class ProductResource(Resource):
    """
    Handles requests to /products/:product_id/

    """

    def __init__(self, *args, **kwargs) -> None:
        self.product_service: ProductService = kwargs["product_service"]

    def get(self, product_id: int):
        product = self.product_service.find_product_by_id(product_id)
        return {"product": ProductSchema().dump(product)}

    def put(self, product_id: int):
        ProductSchema().load(request.json)
        self.product_service.update_product(product_id, **request.json)
        return generic_success_response("Product updated")

    def delete(self, product_id: int):
        self.product_service.delete_product(product_id)
        return None, 204
