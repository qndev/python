from moviestore.models.customer import Customer


class Order:
    def __init__(self, order_id: str, customer_id: str, movies: dict, order_date: str):
        self._order_id = order_id
        self._customer_id = customer_id
        self._movies = movies
        self._order_date = order_date

    def get_order_id(self):
        return self._order_id

    def set_order_id(self, order_id):
        self._order_id = order_id

    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def get_movies(self):
        return self._movies

    def set_movies(self, movies):
        self._movies = movies

    def get_order_date(self):
        return self._order_date

    def set_order_date(self, order_date):
        self._order_date = order_date
