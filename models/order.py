class Order:
    def __init__(self, order_id: str, customer_id: str, movie_id: str, days_rental: float, discount: float, order_date: str):
        self._order_id = order_id
        self._customer_id = customer_id
        self._movie_id = movie_id
        self._days_rental = days_rental
        self._discount = discount
        self._order_date = order_date

    def get_order_id(self):
        return self._order_id

    def set_order_id(self, order_id):
        self._order_id = order_id

    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def get_movie_id(self):
        return self._movie_id

    def set_movie_id(self, movie_id):
        self._movie_id = movie_id

    def get_days_rental(self):
        return self._days_rental

    def set_days_rental(self, days_rental):
        self._days_rental = days_rental

    def get_discount(self):
        return self._discount

    def set_discount(self, discount):
        self._discount = discount

    def get_order_date(self):
        return self._order_date

    def set_order_date(self, order_date):
        self._order_date = order_date
