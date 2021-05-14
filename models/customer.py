class Customer:  
    def __init__(self, customer_id = None, name = None, email = None):
        self._customer_id = customer_id
        self._name = name
        self._email = email

    """ _customer_id = None
    _name = None
    _email = None """

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

    """ def set_customer_values(self, customer_id, name, email):
        self._customer_id = customer_id
        self._name = name
        self._email = email """
