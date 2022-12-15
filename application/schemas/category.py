from application.models import Category
from application.extensions import ma, db
from application.schemas.product import ProductSchema


class CategorySchema(ma.SQLAlchemyAutoSchema):
    id = ma.Int(dump_only=True)
    name = ma.String(required=True)
    products = ma.Nested(ProductSchema, many=True, dump_only=True)

    class Meta:
        model = Category
        sqla_session = db.session
        load_instance = True


class CategoryListSchema(ma.SQLAlchemyAutoSchema):
    id = ma.Int(dump_only=True)

    class Meta:
        model = Category
        sqla_session = db.session
        load_instance = True
        exclude = ("products",)
