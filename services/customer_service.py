from utils.file_utils import FileUltils
from models.customer import Customer
from constants import constant


class CustomerService:
    def insert_customer(self, customer_info: Customer):
        data = {
            "id": customer_info.get_customer_id(),
            "name": customer_info.get_name(),
            "email": customer_info.get_email()
        }
        FileUltils.write_data(data, constant.CUSTOMER_RESOURCES_PATH)

    def select_customer(self, email: str) -> bool:
        select_customer_email = FileUltils.get_data(email)
        #print("Service: " + select_customer_email)
        if (email == select_customer_email):
            return True
        return False
