from application.models import Cart, CartItem, Product
from application.extensions import ma, db


class CartItemProductSchema(ma.SQLAlchemyAutoSchema):
    id = ma.Int(dump_only=True)

    class Meta:
        model = Product
        sqla_session = db.session
        load_instance = True
        exclude = ("quantity",)


class CartItemSchema(ma.SQLAlchemyAutoSchema):
    product = ma.Nested(CartItemProductSchema, dump_only=True)
    quantity = ma.Int()
    in_stock = ma.Method("is_available")

    class Meta:
        model = CartItem
        load_instance = True
        sqla_session = db.session
        exclude = ("id",)

    def is_available(self, obj) -> bool:
        return obj.product.quantity > 1


class CartSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(CartItemSchema, many=True, dump_only=True)

    class Meta:
        model = Cart
        sqla_session = db.session
        load_instance = True
        exclude = ("id",)


class AddProductToCartRequestSchema(ma.Schema):
    product_id = ma.Integer(required=True)
    quantity = ma.Integer()


class RemoveProductFromCartRequestSchema(ma.Schema):
    product_id = ma.Integer(required=True)


class PurchaseCartRequestSchema(ma.Schema):
    card_number = ma.String(required=True)
