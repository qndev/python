class Category:

    def __init__(self, cate_id = None, name = None, price = None, description = None):
        self._cate_id = cate_id
        self._name = name
        self._pricce = price
        self._description =description

    def get_cateid(self):
        return self._cate_id

    def set_cate_id(self, cateid):
        self._cate_id = cateid
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    
    def get_price(self):
        return self._pricce

    def set_price(self, price):
        self._pricce = price
    
    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description
