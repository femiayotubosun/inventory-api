from application.models import Product
from application.extensions import db
from application.common.exceptions import ResourceExistsError, ResourceNotFoundError


class ProductService:
    @staticmethod
    def create_product(**kwargs):
        product = Product(**kwargs)
        db_product = ProductService.find_product_by_name(product.name)
        if db_product:
            raise ResourceExistsError("Product with this name already exists")
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def update_product(product_id: int, **kwargs):
        product = ProductService.find_product_by_id(product_id)
        for key, val in kwargs.items():
            setattr(product, key, val)
        db.session.commit()

    @staticmethod
    def delete_product(product_id: int):
        product = ProductService.find_product_by_id(product_id)
        db.session.delete(product)
        db.session.commit()

    @staticmethod
    def find_products():
        # TODO pagination
        return Product.query.all()

    @staticmethod
    def find_product_by_id(product_id: int):
        product = Product.query.get(product_id)
        if product is None:
            raise ResourceNotFoundError("Product with this ID does not exist")
        return product

    @staticmethod
    def find_product_by_name(name: str):
        return Product.query.filter_by(name=name).first()
