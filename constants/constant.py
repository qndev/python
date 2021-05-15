class Constants:

    REGULAR_MAX_DAYS = 3
    CHILD_FAMILY_MAX_DAYS = 5
    BLOCKBUSTER = 2
    REG_DISC_POINTS = 7
    CF_DISC_POINTS = 5
    BLOCK_DISC_POINTS = 10
    EXTRA_NEW_FEES = [1.0, 1.0, 3.0]
    EXTRA_DAY_FEES = [1.5, 1.0, 3.0]
    OPTIONS = ["1", "2"]
    CUSTOMER_RESOURCES_PATH = "/home/quangnd/Python/python-training/resources/customers.json"
    MOVIE_RESOURCES_PATH = "/home/quangnd/Python/python-training/resources/movies.json"
    CATEGORY_RESOURCES_PATH = "/home/quangnd/Python/python-training/resources/categories.json"
    EMPTY_STRING = ""
    ERROR_MESSAGES = "Some thing went wrong, please contact to admin!"
    CUSTOMER_KEYS = ["customers", "id", "name", "email"]
    ORDERS_KEYS = ["orders", "order_id",
                   "customer_id", "movie_id", "order_date"]
    MOVIE_KEYS = ["name", "category_id", "release_month"]
    CATEGORY_KEYS = ["name", "price", "description"]
    MOVIE_SCREEN_DISPLAY = [26, 23, 19, 17]
    INDEX = 0
