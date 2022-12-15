from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user
from application.common.responses import generic_success_response
from application.services import OrderService


class OrderList(Resource):
    @jwt_required
    def get(self):
        data = OrderService.find_user_orders(current_user)
        return generic_success_response("All orders", data)


class OrderResource(Resource):
    @jwt_required
    def get(self, order_id: int):
        data = OrderService.find_one_user_order(current_user, order_id)
        return generic_success_response("One order", data)
