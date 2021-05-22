from typing import Union
from moviestore.models.customer import Customer
from moviestore.utils.file_utils import FileUltils
from moviestore.constants.constant import Constants


class CustomerService:
    def insert_customer(self, customer_info: Customer):
        data = {
            Constants.CUSTOMER_KEYS[1]: customer_info.get_customer_id(),
            Constants.CUSTOMER_KEYS[2]: customer_info.get_name(),
            Constants.CUSTOMER_KEYS[3]: customer_info.get_email(),
            Constants.CUSTOMER_KEYS[4]: 0
        }
        FileUltils.write_customer_data(data)

    def select_customer_data(self, email: str) -> Union[dict, str]:
        customer = FileUltils.read_customer_data(email, False)
        if (isinstance(customer, dict)):
            return customer
        return "False"
