import datetime
import math
from moviestore.models.invoice import Invoice
from moviestore.constants.constant import Constants
from typing import List
from moviestore.models.order import Order
from moviestore.utils.file_utils import FileUltils


class OrderService:
    def order_movies(self, order_items: List[str]) -> list:

        return Order(None, None, None)

    def export_invoice(self, customer_email) -> tuple:
        customer_info = FileUltils.read_customer_data(customer_email, False)
        customer_id = customer_info[Constants.ORDERS_KEYS[2]]
        orders_info = FileUltils.read_orders_data(customer_id)
        category_info = FileUltils.read_category_data()
        movies_info = FileUltils.read_order_movies_data(
            orders_info["movies"]["movie_ids"])

        invoice_data = []

        for movie_id in movies_info:
            invoice = Invoice()
            invoice.set_movie_name(
                movies_info[movie_id][Constants.MOVIE_KEYS[0]])
            invoice.set_category(
                category_info[movies_info[movie_id]["category_id"]]["name"])
            invoice.set_release_month(
                movies_info[movie_id][Constants.MOVIE_KEYS[2]])

            days_rental = float((orders_info["movies"]["days_rental"])[
                orders_info["movies"]["movie_ids"].index(movie_id)])

            invoice.set_days_rental(days_rental)

            category_id = category_info[movies_info[movie_id]["category_id"]]

            price = float(category_id["price"])

            order_date_str = orders_info["order_date"]

            order_date = datetime.datetime.strptime(order_date_str, '%Y/%m/%d')

            release_month_str = movies_info[movie_id]["release_month"]

            release_month = datetime.datetime.strptime(
                release_month_str, '%Y/%m')

            surcharge_new_movie = 0

            surcharge_days = 0

            if (order_date - release_month < 6):
                if (category_id == "CATE001"):
                    if (days_rental > float(3)):
                        surcharge_days = (days_rental > float(3))*1.5
                    surcharge_new_movie = 1
                if (category_id == "CATE002"):
                    if (days_rental > float(5)):
                        surcharge_days = (days_rental > float(5))*1.0
                    surcharge_new_movie = 1
                if (category_id == "CATE003"):
                    if (days_rental > float(2)):
                        surcharge_days = (days_rental > float(2))*3.0
                    surcharge_new_movie = 3

            invoice.set_surcharge_new_movie(surcharge_new_movie)

            invoice.set_surcharge_days(surcharge_days)

            total_price = price + surcharge_new_movie + surcharge_days

            invoice.set_total_pay(total_price)

            discount = 0

            discount_points = int(customer_info["discount_points"])

            if (discount_points > 200):
                discount = 10
                discount_extra_50 = math.ceil((discount_points - 200)/50)*1
                discount = discount + discount_extra_50

            if (discount > 20):
                discount = 20

            if (total_price > 500):
                discount = 10

            total_pay = discount*total_price

            discount_points_after_pay = 0

            if (total_pay >= 100):
                discount_points_after_pay = 10
                discount_points_after_pay = discount_points_after_pay + \
                    math.ceil((total_pay - 100)*5)
            invoice.set_total_pay(total_pay)

            invoice.set_discount(discount)

            invoice_data.append(invoice)

            print("Invoice: ")
            print(invoice)
            print("Discount Points: ")
            print(discount_points_after_pay)

        return customer_info, invoice
