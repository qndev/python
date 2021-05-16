class Customer:
    def __init__(self, customer_id: str, name: str, email: str, discount_points: int):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._discount_points = discount_points

    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_discount_points(self):
        return self._discount_points

    def set_discount_points(self, discount_points):
        self._discount_points = discount_points
