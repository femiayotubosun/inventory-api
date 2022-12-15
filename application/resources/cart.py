from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, current_user
from application.schemas import (
    CartSchema,
    AddProductToCartRequestSchema,
    RemoveProductFromCartRequestSchema,
    PurchaseCartRequestSchema,
)
from application.services import CartService
from application.common.responses import (
    generic_success_response,
    create_resource_success_response,
)


class CartView(Resource):

    """
    Base Resource for all Cart Views. Handles black_box injection of cart_service
    """

    def __init__(self, *args, **kwargs) -> None:
        self.cart_service: CartService = kwargs["cart_service"]


class CartList(CartView):
    @jwt_required()
    def get(self):
        carts = self.cart_service.find_carts()
        data = CartSchema(many=True).dump(carts)
        return generic_success_response("All Carts", data)


class CartResource(CartView):
    @jwt_required()
    def get(self):
        cart = self.cart_service.find_or_create_user_cart(current_user)
        data = CartSchema().dump(cart)
        return generic_success_response("User Cart", data)


class AddCartItemAction(CartView):
    @jwt_required()
    def post(self):
        AddProductToCartRequestSchema().load(request.json)
        self.cart_service.add_product_to_user_cart(current_user, **request.json)
        return generic_success_response("Product Added to Cart")


class RemoveCartItemAction(CartView):
    @jwt_required()
    def post(self):
        RemoveProductFromCartRequestSchema().load(request.json)
        self.cart_service.remove_product_from_user_cart(current_user, **request.json)
        return generic_success_response("Product Removed from Cart")


class PurchaseCartAction(CartView):
    @jwt_required()
    def post(self):
        PurchaseCartRequestSchema().load(request.json)
        self.cart_service.purchase_user_cart(current_user, **request.json)
        return generic_success_response("Purchase Successful")
