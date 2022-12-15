from application.extensions import db


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.relationship("Product")
    product_id = db.Column(db.ForeignKey("product.id"))
    quantity = db.Column(db.Integer, default=1)
    cart = db.relationship("Cart", back_populates="items")
    cart_id = db.Column(db.ForeignKey("cart.id"))


class Cart(db.Model):
    """
    Representation of the Cart
    """

    id = db.Column(db.Integer, primary_key=True)
    items = db.relationship("CartItem", back_populates="cart")
    user = db.relationship("User", back_populates="cart")
    user_id = db.Column(db.ForeignKey("user.id"))
