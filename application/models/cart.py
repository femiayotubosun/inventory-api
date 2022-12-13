from application.extensions import db
from application.models.product import Product

cart_product = db.Table(
    "cart_product",
    db.Column("cart_id", db.ForeignKey("cart.id"), primary_key=True),
    db.Column("product_id", db.ForeignKey("product.id"), primary_key=True),
)


class Cart(db.Model):
    """
    Representation of the Cart
    """

    id = db.Column(db.Integer, primary_key=True)
    products = db.relationship("Product", secondary=cart_product)
    # user
