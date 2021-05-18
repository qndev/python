from moviestore.constants.constant import Constants
from moviestore.models.order import Order


def convert_order_data(order: Order) -> dict:
    order_data = {
        Constants.ORDERS_KEYS[1]: order.get_order_id(),
        Constants.ORDERS_KEYS[2]: order.get_customer_id(),
        Constants.ORDERS_KEYS[4]: order.get_movies(),
        Constants.ORDERS_KEYS[7]: order.get_order_date()
    }
    return order_data
