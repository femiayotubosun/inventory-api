from application.models import Category
from application.models.product import Product
from application.extensions import db
from application.common.exceptions import ResourceNotFoundError, ResourceExistsError


class CategoryService:
    @staticmethod
    def create_category(**kwargs):
        category = Category(**kwargs)
        db.session.add(category)
        db.session.commit()

    @staticmethod
    def find_categories():
        return Category.query.all()

    @staticmethod
    def find_category_by_id(category_id):
        category = Category.query.get(category_id)
        if category is None:
            raise ResourceNotFoundError("Category with this ID does not exist")
        return category

    @staticmethod
    def delete_category(category_id: int):
        category = CategoryService.find_category_by_id(category_id)
        db.session.delete(category)
        db.session.commit()

    @staticmethod
    def update_category(category_id: int, **kwargs):
        category = CategoryService.find_category_by_id(category_id)
        for key, val in kwargs.items():
            setattr(category, key, val)
        db.session.commit()

    @staticmethod
    def create_product_for_category(category_id, **kwargs):
        category = CategoryService.find_category_by_id(category_id)
        product = Product(**kwargs)
        db_product = Product.query.filter_by(name=product.name).first()
        if db_product:
            raise ResourceExistsError("Product with this name already exists")
        product.category = category
        db.session.add(product)
        db.session.commit()
