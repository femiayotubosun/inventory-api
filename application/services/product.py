from application.models import Product
from application.extensions import db


class ProductService:

    @staticmethod
    def create_product(**kwargs):
        product = Product(**kwargs)
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def update_product():
        pass

    @staticmethod
    def find_product_by_id( product_id):
        product = Product.query.get(product_id)
        if not product:
            raise No

    @staticmethod
    def find_products():
        return Product.query.all()

    @staticmethod
    def find_product_by_name():
        pass

    @staticmethod
    def order_product():
        pass