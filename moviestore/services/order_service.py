import datetime
import math
from moviestore.helpers import order_helper
from moviestore.models.customer import Customer
from moviestore.models.invoice import Invoice
from moviestore.constants.constant import Constants
from typing import Dict, List, Tuple, Union
from moviestore.models.order import Order
from moviestore.utils.file_utils import FileUltils


class OrderService:
    def order_movies(self, order: Order) -> bool:
        order_data = order_helper.convert_order_data(order)
        return FileUltils.write_order_data(order_data) == True

    def export_invoice(self, customer_email: str, order_id: str, invoices_flag: bool, order_flag: bool) -> Tuple[Customer, Union[List[Invoice], List[List[Invoice]]]]:
        customer_info = {}
        invoices = []
        customer_info = FileUltils.read_customer_data(customer_email, False)
        customer_id = customer_info["id"]
        orders_info = FileUltils.read_orders_data(
            customer_id, order_id, invoices_flag)
        if (isinstance(orders_info, list) & (order_flag == False)):
            index = 0
            for order_info in orders_info:
                order = order_helper.convert_to_order(order_info)
                order.set_discount_point_order(
                    orders_info[index]["discount_point_order"])
                order_movie_ids = (order.get_movies())["movie_ids"]
                category_info = FileUltils.read_category_data()
                movies_info = FileUltils.read_order_movies_data(
                    order_movie_ids)
                invoice_data = self.get_invoice_data(
                    movies_info, category_info, order, customer_info, order_flag)
                invoices.append(invoice_data)
                index = index + 1
        else:
            order = order_helper.convert_to_order(orders_info)
            order.set_discount_point_order(
                orders_info["discount_point_order"])
            order_movie_ids = (order.get_movies())["movie_ids"]
            category_info = FileUltils.read_category_data()
            movies_info = FileUltils.read_order_movies_data(order_movie_ids)
            invoice_data = self.get_invoice_data(
                movies_info, category_info, order, customer_info, order_flag)
            invoices = invoice_data

        """ orders = order_helper.convert_to_orders(orders_info)
        order_movie_ids = order_helper.extract_order_movie_ids(orders)
        points_after_payment = self.calculate_points(total_pays) """

        return customer_info, invoices

    def get_invoice_data(self, movies_info: dict, category_info: dict, order: Order, customer_info: dict, order_flag: bool) -> List[Invoice]:
        invoice_data = []

        total_prices = 0.0

        total_pays = 0.0

        for movie_id in movies_info:
            invoice = Invoice(None, None, None, None, None,
                              None, None, None, None, None)
            invoice.set_order_id(order.get_order_id())
            invoice.set_movie_name(
                movies_info[movie_id][Constants.MOVIE_KEYS[0]])
            invoice.set_category(
                category_info[movies_info[movie_id]["category_id"]]["name"])
            invoice.set_release_month(
                movies_info[movie_id][Constants.MOVIE_KEYS[2]])

            days_rental = float((order.get_movies()["days_rental"])[
                order.get_movies()["movie_ids"].index(movie_id)])

            invoice.set_days_rental(days_rental)

            category_id = movies_info[movie_id]["category_id"]

            price = float(category_info[category_id]["price"])

            invoice.set_price(price)

            order_date_str = order.get_order_date()
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

        discount_points = order.get_discount_point_order()

        discount = self.calculate_discount(discount_points, total_pays)

        if (discount > 0):
            total_pays = total_pays - (discount*total_prices)/100

        invoice.set_total_pay(total_pays)

        invoice.set_discount(discount)

        if (order_flag):
            points_after_order = self.calculate_points(
                total_pays, order, movies_info, customer_info)
            FileUltils.write_customer_points(customer_info, points_after_order)

       # print(test)

        return invoice_data

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

    def calculate_points(self, total_pays: float, order: Order, movies_info: dict, customer_info: dict) -> int:
        discount_points = 0
        points_cate01 = 0
        points_cate02 = 0
        points_cate03 = 0

        if (total_pays >= 100):
            discount_points = 10
            discount_points = discount_points + \
                math.floor(((total_pays - 100)*5)/100)
        movie_ids = order.get_movies()["movie_ids"]
        for movie_id in movie_ids:
            category_id = movies_info[movie_id]["category_id"]
            if (category_id == "CATE001"):
                points_cate01 = 7
            if (category_id == "CATE002"):
                points_cate02 = 5
            if (category_id == "CATE003"):
                points_cate03 = 10
        return discount_points + points_cate01 + points_cate02 + points_cate03
