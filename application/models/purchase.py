from application.extensions import db
from application.models.product import Product


class OrderItem(db.Model):
    id = (db.Column(db.Integer, primary_key=True),)
    product_id = db.Column(db.ForeignKey("product.id"))
    product = db.relationship("Product")
    quantity = db.Integer()

    order = db.relationship("Order", back_populates="items")
    order_id = db.Column(db.ForeignKey("order.id"))


class Order(db.Model):
    id = db.Column()
    items = db.relationship("OrderItem", back_populates="order")
    amount = db.Integer()
