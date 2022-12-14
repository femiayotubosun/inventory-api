from application.models import Cart, Product, CartItem
from application.extensions import db
from application.common.exceptions import (
    BadRequestError,
    ResourceNotFoundError,
    InternalServerError,
)
from .payment import PaymentService


class CartService:
    @staticmethod
    def create_cart(**kwargs):
        cart = Cart(**kwargs)

        # db_cart = CartService.get_cart_by_user(cart.user)
        # if db_cart:
        #     raise ResourceExistsError("Cart already exists for this user")

        db.session.add(cart)
        db.session.commit()

    @staticmethod
    def find_carts():
        return Cart.query.all()

    @staticmethod
    def find_cart_by_user(*args, **kwargs) -> Cart:
        return Cart.query.filter_by(user=kwargs["user"]).first()

    @staticmethod
    def find_cart_by_id(cart_id: int) -> Cart:
        cart = Cart.query.get(cart_id)
        if cart is None:
            raise ResourceNotFoundError("Cart with this ID does not exist")
        return cart

    @staticmethod
    def is_product_in_cart(cart_id, product_id) -> bool:
        cart_item = CartItem.query.filter_by(
            product_id=product_id, cart_id=cart_id
        ).first()
        return True if cart_item else False

    @staticmethod
    def add_product_to_cart(cart_id, **kwargs):
        cart = CartService.find_cart_by_id(cart_id)
        product = Product.query.get(kwargs["product_id"])
        if product is None:
            raise ResourceNotFoundError("Product with this ID does not exist")

        if CartService.is_product_in_cart(cart.id, product.id):
            cart_item = CartItem.query.filter_by(product=product, cart=cart).first()
            if "quantity" in kwargs:
                cart_item.quantity = kwargs["quantity"]
        else:
            cart_item = CartItem()
            cart_item.product = product
            if "quantity" in kwargs:
                cart_item.quantity = kwargs["quantity"]
            db.session.add(cart_item)
            cart.items.append(cart_item)
        db.session.commit()

    @staticmethod
    def remove_product_from_cart(cart_id, **kwargs):
        cart = CartService.find_cart_by_id(cart_id)
        product = Product.query.get(kwargs["product_id"])
        if product is None:
            raise ResourceNotFoundError("Product with this ID does not exist")
        if not CartService.is_product_in_cart(cart.id, product.id):
            raise BadRequestError("Product is not in cart")

        cart_item = CartItem.query.filter_by(product=product, cart=cart).first()
        cart.items.remove(cart_item)
        db.session.commit()

    # TODO Purchase Cart

    @staticmethod
    def purchase_cart_item(cart_item: CartItem):
        product: Product = cart_item.product
        quantity = cart_item.quantity

        if quantity > product.quantity:
            raise Exception()
        product.quantity -= quantity

    @staticmethod
    def purchase_cart(cart_id, **kwargs):
        cart: Cart = CartService.find_cart_by_id(cart_id)
        charge = 0
        try:
            for item in cart.items:
                charge += item.quantity * item.product.price
                CartService.purchase_cart_item(item)
                db.session.commit()

            if not PaymentService.process_payment():
                raise InternalServerError("Something went wrong with the payment")
        except:
            db.session.rollback()
