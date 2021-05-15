import json
from config import Config
from constants.constant import Constants


class FileUltils:

    @staticmethod
    def write_customer_data(model: dict):
        logger = Config.logger(__name__)
        try:
            with open(Constants.CUSTOMER_RESOURCES_PATH) as file:
                data = json.load(file)
                temp = data[Constants.CUSTOMER_KEYS[0]]
                temp.append(model)
            with open(Constants.CUSTOMER_RESOURCES_PATH, "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError as fnf:
            logger.error(fnf)
            print(Constants.ERROR_MESSAGES)
        except Exception as e:
            logger.error(e)
            print(Constants.ERROR_MESSAGES)

    @staticmethod
    def read_customer_data(email: str) -> str:
        logger = Config.logger(__name__)
        try:
            with open(Constants.CUSTOMER_RESOURCES_PATH) as file:
                data = json.load(file)
                customers = data["customers"]
                for customer in customers:
                    if(customer["email"] == email):
                        return email
                return Constants.EMPTY_STRING
        except FileNotFoundError as fnf:
            print(Constants.ERROR_MESSAGES)
            logger.error(fnf)
        except Exception as e:
            logger.error(e)
            print(Constants.ERROR_MESSAGES)

    @staticmethod
    def read_movies_data() -> tuple:
        logger = Config.logger(__name__)
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
        except Exception as e:
            logger.error(e)
            print(Constants.ERROR_MESSAGES)
