import logging
import logging.config
import uuid
from constants import constant
from datetime import datetime
from models.customer import Customer
from services.customer_service import CustomerService
from utils.string_utils import StringUtils

def main():
    print("||===============================================================================================||")
    print("||                                                                                               ||")
    print("||                                      /\     /\                                                ||")
    print("||                                     /  \   /  \                                               ||")
    print("||                                    / /\ \_/ /\ \                                              ||")
    print("||                                   / /  \   /  \ \  USOL-VN                                    ||")
    print("||                                  /_/    \_/    \_\OVIE STORE                                  ||")
    print("||                                                                                               ||")
    print("||***********************************************************************************************||")
    print("||                              Please select one of these options                               ||")
    print("||***********************************************************************************************||")
    print("||                                                                                               ||")
    print("||                              1. If you already have an account                                ||")
    print("||                              2. If you don't have an account                                  ||")
    print("||                                                                                               ||")
    print("||===============================================================================================||")
    print("")

    application_running = True

    while application_running:
        selected_option = input("Please select an option: ").strip()
        if (selected_option in constant.OPTIONS):
            application_running = False
        else:
            #logger.error(f"Option {selected_option} can not resolved")
            print("Sorry please select correct the option (1 or 2)!")

    if (selected_option == constant.OPTIONS[1]):
        print("Create your new account")
        creating_account = True;
        customer_info = Customer(None, None, None)

        while creating_account:
            creating_name = True;

            while creating_name:
                customer_name = input("Please enter your name: ")
                if ((StringUtils.check_for_blanks(customer_name)) == False):
                    customer_info.set_name(customer_name)
                    creating_name = False

            while creating_account:
                customer_email = input("Please enter your email: ")
                if ((StringUtils.check_for_blanks(customer_email)) == False):
                    customer_info.set_email(customer_email)
                    creating_account = False
            customer_info.set_customer_id("CUS-" + str(uuid.uuid1()))
        customer_service = CustomerService()
        customer_service.create_customer(customer_info)

if __name__ == "__main__":
    main()
