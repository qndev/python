import logging
import logging.config
from constants import constant
from helpers import (customer_helper, print_helper)


def main():
    print_helper.print_header()
    print_helper.print_options()

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
        customer_helper.set_customer_values()

    if (selected_option == constant.OPTIONS[0]):
        print("Login")
        if(customer_helper.exists_customer()):
            print_helper.print_header()
            print_helper.print_movie_banner()
            return True


if __name__ == "__main__":
    main()
