from application.models import Category
from application.extensions import db
from application.common.exceptions import ResourceNotFoundError


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
        print("finding cat")

        category = Category.query.get(category_id)
        if category is None:
            raise ResourceNotFoundError("Category with this ID does not exist")
        return category

        # except:
        #     print("raised")
        #     raise ResourceNotFoundError("Category with this ID does not exist")

    @staticmethod
    def delete_category(category_id):
        category = CategoryService.find_category_by_id(category_id)
        db.session.delete(category)
        db.session.commit()

    @staticmethod
    def update_category(category_id, **kwargs):
        category = CategoryService.find_category_by_id(category_id)
        category.name = kwargs["name"]
        db.session.commit()
