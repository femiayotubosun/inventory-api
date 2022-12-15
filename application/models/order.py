from application.extensions import db


class Order(db.Model):
    """
    Order Representation
    """

    id = db.Column(db.Integer, primary_key=True)
    charge = db.Column(db.Float)
    cart = db.relationship("Cart")
    cart_id = db.Column(db.ForeignKey("cart.id"))
