from moviestore.services.order_service import OrderService
import os
import uuid
import tempfile
from moviestore.constants.constant import Constants
from moviestore.services.movie_service import MoveService
from moviestore.helpers import (customer_helper, movie_helper, print_helper)
from moviestore.configs.configure_application import ConfigureApplication


class Program:

    def execute(self, root_dir: str):
        logger = ConfigureApplication.logger(__name__)
        logger.info("Started Application")

        separator_temp_filename = "-"
        session_user_id = str(uuid.uuid1())
        prefix_file_name = session_user_id + separator_temp_filename
        temp_dir = root_dir + "/moviestore/temp"
        tempfile.tempdir = temp_dir
        temp_file = tempfile.NamedTemporaryFile(mode="w+",
                                                prefix=prefix_file_name,
                                                dir=temp_dir,
                                                delete=False)
        print("Current temp directory:", tempfile.gettempdir())
        temp_file.write(session_user_id)
        temp_file.seek(0)
        print(temp_file.read())
        temp_file.close()
        # os.unlink(temp_file.name)
        # os.path.exists(temp_file.name)

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
            self.create_account()

        if (selected_option == Constants.OPTIONS[0]):
            self.authenticate_account()

        if (selected_option == "3"):
            self.get_innvoice("nguyen.dinh.quang@gmail.com")

        logger.info("Finished Application")

        self.exit_application(Constants.CONFIRM_EXITING_APPLICATION)

    def create_account(self):
        print("Create your new account ...")
        customer_helper.set_customer_values()
        print("Your account created successfully!\nDo you want to continute (Y/n)")
        self.continue_application()

    def authenticate_account(self):
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
                order_confirmation = input(
                    "Do you wamt to order movies (Y/n): ")
                if ((order_confirmation == "Y") or (order_confirmation == "y")):
                    self.order_movies()
                if (order_confirmation == "n"):
                    order_confirm_flag = False
                    self.execute()
            return None
        else:
            print("Your email dose not exists!\nDo you want to continute (Y/n)")
            self.continue_application()

    def get_innvoice(self, email: str):
        order_service = OrderService()
        order_service.export_invoice(email)
        self.exit_application(Constants.CONFIRM_EXITING_APPLICATION)

    def continue_application(self):
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
                        self.execute()
                    if (decisions == "2"):
                        decisions_flag = False
                        self.authenticate_account()
            if (continue_input == "n"):
                continue_flag = False
                self.exit_application(continue_input)

    def order_movies(self):
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
                    self.execute()
            if ((movie_orders == "yes") & bool(orders)):
                ordering_flag = False
            if (movie_orders == "exit"):
                if (bool(orders)):
                    cancel_ordered = input(
                        "You orderd movies, Are you sure want to cancel (Y/n): ")
                    if (cancel_ordered == "Y"):
                        ordering_flag = False
                        self.execute()
                    if (cancel_ordered == "n"):
                        continue
                ordering_flag = False
                self.exit_application(Constants.CONFIRM_EXITING_APPLICATION)
            if ((movie_orders != "yes") and (movie_orders != "exit")):
                orders.append(movie_orders)
                print(orders)
        print(orders)
        return None

    def payment_movies(self):
        return 0

    def user_input(self, messages: str):
        return input(messages)

    def exit_application(self, confim: str):
        if (confim == Constants.EXIT_APPLICATION):
            print("Good bye!")
            logger = ConfigureApplication.logger(__name__)
            logger.info("Customer exited system")
            exit()
