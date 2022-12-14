from application.extensions import db


class Category(db.Model):
    """
    Category Representation
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    products = db.relationship("Product", back_populates="category")
