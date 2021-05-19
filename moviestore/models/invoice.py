class Invoice:
    def __init__(self, order_id: str, movie_name: str, category: str, release_month: str, days_rental: float, price: float, surcharge_new_movie: float, surcharge_days: float, discount: int, total_pay: float) -> None:
        self._order_id = order_id
        self._movie_name = movie_name
        self._category = category
        self._release_month = release_month
        self._days_rental = days_rental
        self._price = price
        self._surcharge_new_movie = surcharge_new_movie
        self._surcharge_days = surcharge_days
        self._discount = discount
        self._total_pay = total_pay

    def get_order_id(self):
        return self._order_id

    def set_order_id(self, order_id):
        self._order_id = order_id

    def get_movie_name(self):
        return self._movie_name

    def set_movie_name(self, movie_name):
        self._movie_name = movie_name

    def get_category(self):
        return self._category

    def set_category(self, category):
        self._category = category

    def get_release_month(self):
        return self._release_month

    def set_release_month(self, release_month):
        self._release_month = release_month

    def get_days_rental(self):
        return self._days_rental

    def set_days_rental(self, days_rental):
        self._days_rental = days_rental

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_surcharge_new_movie(self):
        return self._surcharge_new_movie

    def set_surcharge_new_movie(self, surcharge_new_movie):
        self._surcharge_new_movie = surcharge_new_movie

    def get_surcharge_days(self):
        return self._surcharge_days

    def set_surcharge_days(self, surcharge_days):
        self._surcharge_days = surcharge_days

    def get_discount(self):
        return self._discount

    def set_discount(self, discount):
        self._discount = discount

    def get_total_pay(self):
        return self._total_pay

    def set_total_pay(self, total_pay):
        self._total_pay = total_pay
