from application.models import Order
from application.extensions import ma, db


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        exclude = ["user"   ]
