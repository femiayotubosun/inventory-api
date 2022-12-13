from application.models import Cart
from application.extensions import db
from application.services.product import ProductService


class CartService:
    @staticmethod
    def create_cart(*args, **kwargs):
        cart = Cart(**kwargs)
        db.session.add(cart)
        db.session.commit()

    @staticmethod
    def get_cart_by_user(*args, **kwargs) -> Cart:
        return Cart.query.filter_by(user=kwargs["user"]).first()

    @staticmethod
    def add_product_to_user_cart(*args, **kwargs):
        cart = CartService.get_cart_by_user(kwargs["user"])
        product = ProductService.find_product_by_id(kwargs["product_id"])
        cart.products.append(product)
        db.session.commit()

    @staticmethod
    def remove_product_from_user_cart(*args, **kwargs):
        cart = CartService.get_cart_by_user(kwargs["user"])
        product = ProductService.find_product_by_id(kwargs["product_id"])
        cart.products.remove(product)
        db.session.commit()
