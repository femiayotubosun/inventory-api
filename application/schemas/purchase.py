from application.extensions import db, ma


# class OrderSchema(ma.SQLAlchemyAutoSchema):


class OrderItemRequestSchema(ma.Schema):
    """
    Shape of one order item
    """

    product_id = ma.fields.Integer()
    quantity = ma.fields.Integer()


class OrderRequestSchema(ma.Schema):
    """
    Shape of order request
    """

    items = ma.fields.Nested(OrderItemRequestSchema, many=True)
