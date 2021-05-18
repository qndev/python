import json
import copy
from moviestore.models.customer import Customer
from moviestore.models.movie import Movie
from moviestore.models.order import Order
from typing import Union
from moviestore.configs.configure_application import ConfigureApplication
from moviestore.constants.constant import Constants

logger = ConfigureApplication.logger(__name__)


class FileUltils:

    @staticmethod
    def write_customer_data(model: dict) -> Union[bool, FileNotFoundError, Exception]:
        try:
            with open(Constants.CUSTOMER_RESOURCES_PATH) as file:
                data = json.load(file)
                temp = data[Constants.CUSTOMER_KEYS[0]]
                temp.append(model)
            with open(Constants.CUSTOMER_RESOURCES_PATH, "w") as file:
                json.dump(data, file, indent=4)
            return True
        except FileNotFoundError as fnf:
            logger.error(fnf)
            print(Constants.ERROR_MESSAGES)
            return fnf
        except Exception as e:
            logger.error(e)
            print(Constants.ERROR_MESSAGES)
            return e

    @staticmethod
    def read_customer_email(email: str) -> Union[str, FileNotFoundError, Exception]:
        try:
            with open(Constants.CUSTOMER_RESOURCES_PATH) as file:
                data = json.load(file)
                customers = data["customers"]
                for customer in customers:
                    if(customer["email"] == email):
                        return email
                return Constants.EMPTY_STRING
        except FileNotFoundError as fnf:
            logger.error(fnf)
            print(Constants.ERROR_MESSAGES)
            return fnf
        except Exception as e:
            logger.error(e)
            print(Constants.ERROR_MESSAGES)
            return e

    @staticmethod
    def read_movies_data() -> Union[tuple, FileNotFoundError, Exception]:
        movie_data = {}
        category_data = {}
        try:
            with open(Constants.MOVIE_RESOURCES_PATH, "r") as movie_file:
                movie_data = json.load(movie_file)
            with open(Constants.CATEGORY_RESOURCES_PATH, "r") as category_file:
                category_data = json.load(category_file)
            return movie_data, category_data
        except FileNotFoundError as fnf:
            logger.error(fnf)
            print(Constants.ERROR_MESSAGES)
            return fnf
        except Exception as e:
            logger.error(e)
            print(Constants.ERROR_MESSAGES)
            return e

    @staticmethod
    def read_customer_data(email: str, email_only: bool) -> Union[dict, str, FileNotFoundError, Exception]:
        try:
            with open(Constants.CUSTOMER_RESOURCES_PATH) as file:
                data = json.load(file)
                customers = data["customers"]
                for customer in customers:
                    if(customer["email"] == email):
                        if (email_only):
                            return email
                        else:
                            return customer
                return Constants.EMPTY_STRING
        except FileNotFoundError as fnf:
            logger.error(fnf)
            print(Constants.ERROR_MESSAGES)
            return fnf
        except Exception as e:
            logger.error(e)
            print(Constants.ERROR_MESSAGES)
            return e

    @staticmethod
    def read_orders_data(customer_id: str, order_id: str) -> Union[Order, FileNotFoundError, Exception]:
        orders_data = []
        try:
            with open(Constants.CUSTOMER_RESOURCES_PATH, "r") as customer_file:
                data = json.load(customer_file)
                orders_data = data[Constants.ORDERS_KEYS[0]]
                for order_item in orders_data:
                    if ((order_item[Constants.ORDERS_KEYS[2]] == customer_id) & (order_item["order_id"] == order_id)):
                        order = Order(None, None, None, None)
                        movies = {
                            "movie_ids": (order_item["movies"])["movie_ids"],
                            "days_rental": (order_item["movies"])["days_rental"]
                        }
                        order.set_order_id(order_item["order_id"])
                        order.set_movies(movies)
                        order.set_order_date(order_item["order_date"])
                        customer_file.close()
                        return order
        except FileNotFoundError as fnf:
            logger.error(fnf)
            print(Constants.ERROR_MESSAGES)
            return fnf
        except Exception as e:
            logger.error(e)
            print(Constants.ERROR_MESSAGES)
            return e

    @staticmethod
    def read_category_data() -> Union[dict, FileNotFoundError, Exception]:
        category_data = {}
        try:
            with open(Constants.CATEGORY_RESOURCES_PATH, "r") as category_file:
                category_data = json.load(category_file)
            return category_data
        except FileNotFoundError as fnf:
            logger.error(fnf)
            print(Constants.ERROR_MESSAGES)
            return fnf
        except Exception as e:
            logger.error(e)
            print(Constants.ERROR_MESSAGES)
            return e

    @staticmethod
    def read_order_movies_data(movie_ids: list) -> Union[dict, FileNotFoundError, Exception]:
        order_movies_data = {}
        try:
            with open(Constants.MOVIE_RESOURCES_PATH, "r") as movie_file:
                movie_data = json.load(movie_file)
                order_movies_data = copy.deepcopy(movie_data)
                for movie_id in movie_data:
                    if (movie_id not in movie_ids):
                        order_movies_data.pop(movie_id)
            return order_movies_data
        except FileNotFoundError as fnf:
            logger.error(fnf)
            print(Constants.ERROR_MESSAGES)
            return fnf
        except Exception as e:
            logger.error(e)
            print(Constants.ERROR_MESSAGES)
            return e

    @staticmethod
    def write_order_data(order: dict) -> Union[bool, FileNotFoundError, Exception]:
        try:
            with open(Constants.CUSTOMER_RESOURCES_PATH) as file:
                data = json.load(file)
                temp = data[Constants.ORDERS_KEYS[0]]
                temp.append(order)
            with open(Constants.CUSTOMER_RESOURCES_PATH, "w") as file:
                json.dump(data, file, indent=4)
            return True
        except FileNotFoundError as fnf:
            logger.error(fnf)
            print(Constants.ERROR_MESSAGES)
            return fnf
        except Exception as e:
            logger.error(e)
            print(Constants.ERROR_MESSAGES)
            return e
