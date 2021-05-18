import datetime
import math
from moviestore.models.customer import Customer
from moviestore.models.invoice import Invoice
from moviestore.constants.constant import Constants
from typing import List, Tuple
from moviestore.models.order import Order
from moviestore.utils.file_utils import FileUltils


class OrderService:
    def order_movies(self, order_items: List[str]) -> list:

        return Order(None, None, None)

    def export_invoice(self, customer_email: str) -> Tuple[Customer, List[Invoice]]:
        customer_info = {}
        customer_info = FileUltils.read_customer_data(customer_email, False)
        customer_id = customer_info["id"]
        orders_info = FileUltils.read_orders_data(customer_id, "ORDER001")
        category_info = FileUltils.read_category_data()
        movies_info = FileUltils.read_order_movies_data(
            (orders_info.get_movies())["movie_ids"])

        invoice_data = []

        total_prices = 0.0

        total_pays = 0.0

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

            invoice.set_days_rental(days_rental)

            category_id = movies_info[movie_id]["category_id"]

            price = float(category_info[category_id]["price"])

            invoice.set_price(price)

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
            if (new_movie):
                if (category_id == "CATE001"):
                    if (days_rental > 3):
                        surcharge_days = surcharge_days + \
                            (days_rental - 3)*1
                    surcharge_new_movie = surcharge_new_movie + 1
                if (category_id == "CATE002"):
                    if (days_rental > 5):
                        surcharge_days = surcharge_days + \
                            (days_rental - 5)*1
                    surcharge_new_movie = surcharge_new_movie + 1
                if (category_id == "CATE003"):
                    if (days_rental > 2):
                        surcharge_days = surcharge_days + \
                            (days_rental - 2)*3
                    surcharge_new_movie = surcharge_new_movie + 3
            else:
                if ((category_id == "CATE001") & (days_rental > 3)):
                    surcharge_days = surcharge_days + \
                        (days_rental - 3)*1
                if ((category_id == "CATE002") & (days_rental > 5)):
                    surcharge_days = surcharge_days + \
                        (days_rental - 5)*1
                if ((category_id == "CATE003") & (days_rental > 2)):
                    surcharge_days = surcharge_days + \
                        (days_rental - 2)*3

            invoice.set_surcharge_new_movie(surcharge_new_movie)

            invoice.set_surcharge_days(surcharge_days)

            total_price = price + surcharge_new_movie + surcharge_days

            total_prices = total_prices + total_price

            total_pays = total_prices

            invoice_data.append(invoice)

        discount_points = int(customer_info["discount_points"])

        discount = self.calculate_discount(discount_points, total_pays)

        if (discount > 0):
            total_pays = total_pays - (discount*total_prices)/100

        invoice.set_total_pay(total_pays)

        invoice.set_discount(discount)

        points_after_payment = self.calculate_points(total_pays)

        return customer_info, invoice_data

    def calculate_order_price(self, ):
        return 0

    def calculate_discount(self, discount_points: int, total_pays: float) -> float:
        discount = 0
        if (discount_points > 200):
            discount = 10
            discount_extra_50 = math.floor((discount_points - 200)/50)*1
            discount = discount + discount_extra_50
        else:
            discount = discount + math.floor(discount_points/100)*5

        if (discount > 20):
            discount = 10

        if (total_pays > 500):
            discount = 10

        return discount

    def calculate_points(self, total_pays: float) -> int:
        discount_points = 0

        if (total_pays >= 100):
            discount_points = 10
            discount_points = discount_points + \
                math.floor((total_pays - 100)*5)

        return discount_points
