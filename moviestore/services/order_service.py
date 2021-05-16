from moviestore.constants.constant import Constants
from typing import List
from moviestore.models.order import Order
from moviestore.utils.file_utils import FileUltils


class OrderService:
    def order_movies(self, order_items: List[str]) -> list:

        return Order(None, None, None, None, None)

    def export_invoice(self, customer_email) -> tuple:
        customer_info = FileUltils.read_customer_data(customer_email, False)
        customer_id = customer_info[Constants.ORDERS_KEYS[2]]
        orders_info = FileUltils.read_orders_data(customer_id)
        category_info = FileUltils.read_category_data()
        movies_info = FileUltils.read_order_movies_data(
            orders_info["movies"]["movie_ids"])
        return customer_info, 0
