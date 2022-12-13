from application.models import Product
from application.extensions import ma, db


class ProductSchema(ma.SQLAlchemyAutoSchema):
    id = ma.Int(dump_only=True)
    name = ma.String(required=True)
    quantity = ma.Int(required=True, load_only=True)
    price = ma.Int(required=True)

    class Meta:
        model = Product
        sqla_session = db.session
        load_instance = True
