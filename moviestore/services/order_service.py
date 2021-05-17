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

    def export_invoice(self, customer_email: str) -> tuple:
        customer_info = FileUltils.read_customer_data(customer_email, False)
        customer_id = customer_info["id"]
        print(customer_id)
        orders_info = FileUltils.read_orders_data(customer_id, "ORDER001")
        category_info = FileUltils.read_category_data()
        print(orders_info.get_movies())
        movies_info = FileUltils.read_order_movies_data(
            (orders_info.get_movies())["movie_ids"])

        invoice_data = []

        total_prices = 0.0

        total_pays = 0.0

        total_discount = 0

        for movie_id in movies_info:
            invoice = Invoice(None, None, None, None,
                              None, None, None, None, None)
            invoice.set_movie_name(
                movies_info[movie_id][Constants.MOVIE_KEYS[0]])
            invoice.set_category(
                category_info[movies_info[movie_id]["category_id"]]["name"])
            invoice.set_release_month(
                movies_info[movie_id][Constants.MOVIE_KEYS[2]])

            days_rental = float((orders_info.get_movies()["days_rental"])[
                orders_info.get_movies()["movie_ids"].index(movie_id)])

            print("Day rental")
            print(type(days_rental))
            print(days_rental)

            invoice.set_days_rental(days_rental)

            category_id = movies_info[movie_id]["category_id"]

            print("Category ID: ")
            print(category_id)

            price = float(category_info[category_id]["price"])

            order_date_str = orders_info.get_order_date()
            release_month_str = movies_info[movie_id]["release_month"]

            order_date = datetime.datetime.strptime(order_date_str, '%Y/%m/%d')
            release_month = datetime.datetime.strptime(
                release_month_str, '%Y/%m')

            month_order = order_date.month
            year_order = order_date.year

            month_release = release_month.month
            year_release = release_month.year

            surcharge_new_movie = 0
            surcharge_days = 0

            new_movie = False

            if ((year_order == year_release) & ((month_order - month_release) < 6)):
                new_movie = True

            if(year_order != year_release):
                if ((year_order - year_release) == 1) & ((12 - month_release + month_order) < 6):
                    new_movie = True
                else:
                    new_movie = False
            print(new_movie)
            if (new_movie):
                if (category_id == "CATE001"):
                    if (days_rental > float(3)):
                        surcharge_days = surcharge_days + \
                            (days_rental - float(3))*1.5
                    surcharge_new_movie = surcharge_new_movie + 1
                if (category_id == "CATE002"):
                    if (days_rental > float(5)):
                        surcharge_days = surcharge_days + \
                            (days_rental - float(5))*1.0
                    surcharge_new_movie = surcharge_new_movie + 1
                if (category_id == "CATE003"):
                    if (days_rental > float(2)):
                        surcharge_days = surcharge_days + \
                            (days_rental - float(2))*3.0
                    surcharge_new_movie = surcharge_new_movie + 3

            invoice.set_surcharge_new_movie(surcharge_new_movie)

            invoice.set_surcharge_days(surcharge_days)

            print("DXXXXXXXXXXXXXXXXXXXXXX")
            print(surcharge_new_movie)

            print("DXXXXXXXXXXXXXXXXXXXXXX")
            print(surcharge_days)

            total_price = price + surcharge_new_movie + surcharge_days

            print("Price: ")
            print(total_price)

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

            total_prices = total_prices + total_price

            total_pays = total_pays + total_price

            total_discount = total_discount + discount

            # invoice.set_total_pay(total_pay)

            invoice.set_discount(discount)

            invoice_data.append(invoice)

        if (total_discount > 0):
            total_pays = total_pays - (total_discount*total_price)/100

        print("Total Price: ")
        print(total_prices)

        print("Total Pay: ")
        print(total_pays)

        discount_points_after_pay = 0

        if (total_pays >= 100):
            discount_points_after_pay = 10
            discount_points_after_pay = discount_points_after_pay + \
                math.ceil((total_pays - 100)*5)

        return customer_info, invoice
