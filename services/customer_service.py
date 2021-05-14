from utils.file_utils import FileUltils
from models.customer import Customer
from constants import constant


class CustomerService:
    def create_customer(self, customer_info: Customer):
        data = {
            "id" : customer_info.get_customer_id(),
            "name": customer_info.get_name(),
            "email": customer_info.get_email()
        }
        FileUltils.write_data(data, constant.CUSTOMER_RESOURCES_PATH)
