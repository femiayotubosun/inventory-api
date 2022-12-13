from application.models import Cart
from application.extensions import ma, db


class CartSchema(ma.SQLAlchemyAutoSchema):
    id = ma.Int(dump_only=True)
    # products

    class Meta:
        model = Cart
        sqla_session = db.session
        load_instance = True
