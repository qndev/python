import os


class Constants:

    path_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    REGULAR_MAX_DAYS = 3
    CHILD_FAMILY_MAX_DAYS = 5
    BLOCKBUSTER = 2
    REG_DISC_POINTS = 7
    CF_DISC_POINTS = 5
    BLOCK_DISC_POINTS = 10
    EXTRA_NEW_FEES = [1.0, 1.0, 3.0]
    EXTRA_DAY_FEES = [1.5, 1.0, 3.0]
    OPTIONS = ["1", "2", "3"]
    CUSTOMER_RESOURCES_PATH = path_dir + "/resources/customers.json"
    MOVIE_RESOURCES_PATH = path_dir + "/resources/movies.json"
    CATEGORY_RESOURCES_PATH = path_dir + "/resources/categories.json"
    EMPTY_STRING = ""
    ERROR_MESSAGES = "Some thing went wrong, please contact to administrator to fix this!"
    CUSTOMER_KEYS = ["customers", "id", "name", "email"]
    ORDERS_KEYS = ["orders", "order_id", "customer_id", "customer",
                   "movies", "days_rental", "discount", "order_date"]
    # ORDERS_KEYS = ["orders", "order_id",
    #                "customer_id", "movie_id", "order_date"]
    MOVIE_KEYS = ["name", "category_id", "release_month"]
    CATEGORY_KEYS = ["name", "price", "description"]
    MOVIE_SCREEN_DISPLAY = [17, 28, 23, 19, 19]
    INDEX = 0
    CONFIRM_EXITING_APPLICATION = "n"
    EXIT_APPLICATION = "n"
