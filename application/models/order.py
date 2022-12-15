from application.extensions import db


class Order(db.Model):
    """
    Order Representation
    """

    id = db.Column(db.Integer, primary_key=True)
    charge = db.Column(db.Float)
    user = db.relationship("User", back_populates="orders")
    user_id = db.Column(db.ForeignKey("user.id"))
