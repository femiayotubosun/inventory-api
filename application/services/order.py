from application.models import Order, User
from application.extensions import db
from application.common.exceptions import ResourceNotFoundError, UnauthorizedError


class OrderService:
    @staticmethod
    def find_user_orders(user: User):
        return Order.query.filter_by(user=user)

    @staticmethod
    def find_one_user_order(user: User, order_id: int):
        order = Order.query.get(order_id)
        
        if order is None:
            raise ResourceNotFoundError("There is no order with this id")

        if order.user is not user:
            raise UnauthorizedError("You are not authorized to view this resource")

        return order
