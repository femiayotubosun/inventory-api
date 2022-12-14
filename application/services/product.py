from application.models import Product
from application.extensions import db
from application.services.payment import InitializePaymentDTO


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
    def find_product_by_id(product_id):
        product = Product.query.get(product_id)
        if not product:
            raise Exception()

    @staticmethod
    def find_products():
        return Product.query.all()

    @staticmethod
    def find_product_by_name():
        pass

    @staticmethod
    def purchase_product(*args, **kwargs):
        quantity = kwargs["kwargs"]
        product: Product = Product.query.get(kwargs["product_id"])

        if quantity > product.quantity:
            # Not enough in stock
            raise Exception("There is not enough stock")

    @staticmethod
    def update_product_after_purchase(*args, **kwargs):
        ProductService.update_product()
