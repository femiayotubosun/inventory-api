from application.models import Cart, CartItem
from application.extensions import ma, db
from application.schemas.product import ProductSchema


class CartItemSchema(ma.SQLAlchemyAutoSchema):
    id = (ma.Int(dump_only=True),)
    product = ma.Nested(ProductSchema, dump_only=True)
    quantity = ma.Int()
    in_stock = ma.Method("is_available")

    class Meta:
        model = CartItem
        load_instance = True
        sqla_session = db.session

    def is_available(self, obj) -> bool:
        return obj.product.quantity > 1


class CartSchema(ma.SQLAlchemyAutoSchema):
    id = ma.Int(dump_only=True)
    items = ma.Nested(CartItemSchema, many=True, dump_only=True)

    class Meta:
        model = Cart
        sqla_session = db.session
        load_instance = True


class AddProductToCartRequestSchema(ma.Schema):
    product_id = ma.Integer(required=True)
    quantity = ma.Integer()


class RemoveProductFromCartRequestSchema(ma.Schema):
    product_id = ma.Integer(required=True)


class PurchaseCartRequestSchema(ma.Schema):
    card_number = ma.String(required=True)
