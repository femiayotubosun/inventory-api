from application.extensions import db


class Product(db.Model):
    """
    Product Model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)

    @property
    def in_stock(self):
        return self.quantity > 0
