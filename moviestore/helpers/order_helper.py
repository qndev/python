from typing import Any, List
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


def convert_to_order(order_data: dict) -> Order:
    order = Order(None, None, None, None)
    movies = {
        "movie_ids": (order_data["movies"])["movie_ids"],
        "days_rental": (order_data["movies"])["days_rental"]
    }
    order.set_order_id(order_data["order_id"])
    order.set_movies(movies)
    order.set_order_date(order_data["order_date"])

    return order


def convert_to_orders(order_data: list) -> List[Order]:
    orders = []
    for order_item in order_data:
        order = Order(None, None, None, None)
        order.set_order_id(order_item["order_id"])
        movies = {
            "movie_ids": (order_data["movies"])["movie_ids"],
            "days_rental": (order_data["movies"])["days_rental"]
        }
        order.set_movies(movies)
        order.set_order_date(order_item["order_date"])
        orders.append(order)
    return orders


def extract_order_movie_ids(orders: Order) -> list:
    order_movie_ids = []
    for order in orders:
        order_ids = order.get_movies()["movie_ids"]
        for order_id in order_ids:
            if (order_id not in order_movie_ids):
                order_movie_ids.append(order_id)
    return order_movie_ids
