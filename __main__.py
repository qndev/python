from models.movie import Movie
from services.movie_service import MoveService
from constants.constant import Constants
from helpers import (customer_helper, movie_helper, print_helper)
from config import Config
from utils.string_utils import StringUtils

logger = Config.logger(__name__)


def main():

    logger.info("Started Application")

    print_helper.print_header()
    print_helper.print_options()

    application_running = True

    while application_running:
        selected_option = input("Please select an option: ").strip()
        if (selected_option in Constants.OPTIONS):
            application_running = False
        else:
            logger.error(f"Option {selected_option} can not resolved")
            print("Sorry please select correct the option (1 or 2)!")

    if (selected_option == Constants.OPTIONS[1]):
        create_account()

    if (selected_option == Constants.OPTIONS[0]):
        authenticate_account()

    logger.info("Finished Application")


def create_account():
    print("Create your new account ...")
    customer_helper.set_customer_values()
    print("Your account created successfully!\nDo you want to continute (Y/n)")
    continue_application()


def authenticate_account():
    print("Authenticate your account ...")
    if(customer_helper.exists_customer()):
        print_helper.print_header()
        print_helper.print_movie_banner()

        movie_service = MoveService()
        movies = movie_service.select_movies()
        if not bool(movies):
            print("There are no films in the store!")
            return
        no = 1
        sliced_movies = movie_helper.slice_string(movies)
        for movie in sliced_movies:
            print_helper.print_list_movies(movie, no)
            no = no + 1
        print("+--------------------+-----------------------------+------------------------+--------------------+--------------------+")
        order_confirm_flag = True
        while order_confirm_flag:
            order_confirmation = input("Do you wamt to order movies (Y/n): ")
            if ((order_confirmation == "Y") or (order_confirmation == "y")):
                order_movies()
            if (order_confirmation == "n"):
                order_confirm_flag = False
                main()
        return None
    else:
        print("Your email dose not exists!\nDo you want to continute (Y/n)")
        continue_application()


def continue_application():
    continue_flag = True
    while continue_flag:
        continue_input = input("Please select correct option (Y or n): ")
        if ((continue_input == "Y") | (continue_input == "y")):
            continue_flag = False
            print("You want to go home (1) or authenticate acount (2)?")
            decisions_flag = True
            while decisions_flag:
                decisions = input(
                    "Please select correct option (1 or 2): ")
                if (decisions == "1"):
                    decisions_flag = False
                    main()
                if (decisions == "2"):
                    decisions_flag = False
                    authenticate_account()
        if (continue_input == "n"):
            continue_flag = False
            exit_application(continue_input)


def order_movies():
    ordering_flag = True
    orders = []
    print("Note: Confirm order complete movie whenever please enter 'yes' or 'exit' to cancel all movies ordered.")
    while ordering_flag:
        movie_orders = input(
            "Please select movies yourself by choose Movie ID: ")
        if ((movie_orders == "yes") & (not bool(orders))):
            cancel = input(
                "You have not yet ordered any movies, do you want to cancel (Y/n): ")
            if (cancel == "Y"):
                ordering_flag = False
                main()
        if ((movie_orders == "yes") & bool(orders)):
            ordering_flag = False
        if (movie_orders == "exit"):
            if (bool(orders)):
                cancel_ordered = input(
                    "You orderd movies, Are you sure want to cancel (Y/n): ")
                if (cancel_ordered == "Y"):
                    ordering_flag = False
                    main()
                if (cancel_ordered == "n"):
                    continue
            ordering_flag = False
            exit_application("n")
        if ((movie_orders != "yes") and (movie_orders != "exit")):
            orders.append(movie_orders)
            print(orders)
    print(orders)
    return None


def payment_movies():
    return 0


def user_input(messages: str):
    return input(messages)


def exit_application(confim: str):
    if (confim == "n"):
        print("Good bye!")
        logger.info("Customer exited system")
        exit()


if __name__ == "__main__":
    main()
