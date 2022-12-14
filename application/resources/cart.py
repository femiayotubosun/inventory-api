from flask_restful import Resource
from flask import request
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
    def post(self):
        self.cart_service.create_cart()
        return create_resource_success_response("Cart Created"), 201

    def get(self):
        carts = self.cart_service.find_carts()
        data = CartSchema(many=True).dump(carts)
        return generic_success_response("All Carts", data)


class CartResource(CartView):
    def get(self, cart_id: int):
        cart = self.cart_service.find_cart_by_id(cart_id)
        data = CartSchema().dump(cart)
        return generic_success_response("User Cart", data)


class AddCartItemAction(CartView):
    def post(self, cart_id: int):
        AddProductToCartRequestSchema().load(request.json)
        self.cart_service.add_product_to_cart(cart_id, **request.json)
        return generic_success_response("Product Added to Cart")


class RemoveCartItemAction(CartView):
    def __init__(self, *args, **kwargs) -> None:
        self.cart_service: CartService = kwargs["cart_service"]

    def post(self, cart_id: int):
        RemoveProductFromCartRequestSchema().load(request.json)
        self.cart_service.remove_product_from_cart(cart_id, **request.json)
        return generic_success_response("Product Removed from Cart")


class PurchaseCartAction(CartView):
    def post(self, cart_id: int, **kwargs):
        PurchaseCartRequestSchema().load(request.json)
        self.cart_service.purchase_cart(cart_id, **request.json)
        return generic_success_response("Purchase Successful")
