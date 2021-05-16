import uuid
from moviestore.models.customer import Customer
from moviestore.utils.string_utils import StringUtils
from moviestore.services.customer_service import CustomerService
from moviestore.configs.configure_application import ConfigureApplication

customer_service = CustomerService()

logger = ConfigureApplication.logger(__name__)


def set_customer_values():
    logger.info("Helper class")
    customer = Customer(None, None, None, None)
    creating_account = True
    while creating_account:
        creating_name = True
        while creating_name:
            customer_name = input("Please enter your name: ")
            if ((StringUtils.check_for_blanks(customer_name)) == False):
                customer.set_name(customer_name)
                creating_name = False

        while creating_account:
            customer_email = input("Please enter your email: ")
            if ((StringUtils.check_for_blanks(customer_email)) == False):
                customer.set_email(customer_email)
                creating_account = False
        customer.set_customer_id("cs400881-" + str(uuid.uuid1()))
    customer_service.insert_customer(customer)


def exists_customer() -> bool:
    logging_in = True
    imput_email = ""
    while logging_in:
        imput_email = input("Please enter your email: ")
        if ((StringUtils.check_for_blanks(imput_email)) == False):
            logging_in = False
    exists_customer = customer_service.select_customer_email(imput_email)
    if (exists_customer):
        return True
    return False
