from flask import request
from flask_restful import Resource
from application.services import ProductService


class ProductResource(Resource):
    def __init__(self, **kwargs):
        self.product_service: ProductService = kwargs['product_service']

    def get(self, product_id):
        product = self.product_service.find_product_by_id(product_id)
        return {
            'product': product
        }

