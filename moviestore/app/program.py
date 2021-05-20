from datetime import datetime, date
from moviestore.models.order import Order
import os
import uuid
import tempfile
from moviestore.constants.constant import Constants
from moviestore.services.movie_service import MoveService
from moviestore.services.order_service import OrderService
from moviestore.helpers import (customer_helper, movie_helper, print_helper)
from moviestore.configs.configure_application import ConfigureApplication


class Program:

    def execute(self):
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logger = ConfigureApplication.logger(__name__)
        logger.info("Started Application")

        separator_temp_filename = "-"
        session_user_id = str(uuid.uuid1())
        prefix_file_name = session_user_id + separator_temp_filename
        temp_dir = root_dir + "/temp"

        print(root_dir)
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
        os.unlink(temp_file.name)
        os.path.exists(temp_file.name)

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
            self.get_innvoice("test", "GET_IVOICES", False)

        self.exit_application(Constants.CONFIRM_EXITING_APPLICATION)

    def create_account(self):
        print("Create your new account ...")
        customer_helper.set_customer_values()
        print("Your account created successfully!\nDo you want to continute (Y/n)")
        self.continue_application()

    def authenticate_account(self):
        print("Authenticate your account ...")
        customer_data = customer_helper.exists_customer()
        if(isinstance(customer_data, dict)):
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
            order_confirm_flag = True
            while order_confirm_flag:
                order_confirmation = input(
                    "Do you want to order movies (Y/n): ")
                if ((order_confirmation == "Y") or (order_confirmation == "y")):
                    self.order_movies(customer_data)
                if (order_confirmation == "n"):
                    order_confirm_flag = False
                    self.execute()
            return None
        else:
            print("Your email dose not exists!\nPlease input correct your email address:")
            self.authenticate_account()

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

    def order_movies(self, customer_data: dict):
        ordering_flag = True
        orders = []
        day_rentals = []
        ordered_id = ""
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
                ordered_id = self.make_order(
                    customer_data, orders, day_rentals)
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
                self.execute()
            if ((movie_orders != "yes") and (movie_orders != "exit")):
                if (self.validate_movie_input(movie_orders)):
                    orders.append(movie_orders)
                    valid_day_flag = True
                    while valid_day_flag:
                        day_rental = input(
                            "Enter number of days you want to watch: ")
                        if (self.validate_day_rental_input(day_rental)):
                            valid_day_flag = False
                            day_rentals.append(float(day_rental))
                        else:
                            print("Invalid day rental!")
                else:
                    print("Your movie you entered does not exists!")
        if (ordered_id != Constants.ERROR):
            self.get_innvoice(customer_data["email"], ordered_id, True)
        else:
            print(Constants.ERROR_MESSAGES)
            self.exit_application(Constants.EXIT_APPLICATION)
        print(day_rentals)
        print(orders)

    def make_order(self, customer_data: dict, order_movies: list, days_rental: list) -> str:
        order = Order(None, None, None, None, None)
        order_id = str(uuid.uuid1())
        order.set_order_id(order_id)
        order.set_customer_id(customer_data["id"])
        order.set_movies({
            "movie_ids": order_movies,
            "days_rental": days_rental
        })
        order.set_discount_point_order(customer_data["discount_points"])
        today = date.today()
        today = today.strftime("%Y/%m/%d")
        order.set_order_date(today)

        order_service = OrderService()
        if order_service.order_movies(order):
            print("Ordered movies!")
            return order_id
        else:
            return Constants.ERROR

    def get_innvoice(self, email: str, order_id: str, order_flag: bool):
        order_service = OrderService()
        if (order_id != "GET_IVOICES"):
            customer_details, invoice = order_service.export_invoice(
                email, order_id, False, order_flag)
            print_helper.print_invoices(customer_details, invoice)
        else:
            customer_details, invoice = order_service.export_invoice(
                email, order_id, True, order_flag)
            print_helper.print_invoices(customer_details, invoice)
        self.exit_application(Constants.CONFIRM_EXITING_APPLICATION)

    def validate_movie_input(self, movie_id: str) -> bool:
        if (movie_id in ["MOV001", "MOV002", "MOV003", "MOV004", "MOV005"]):
            return True
        return False

    def validate_day_rental_input(self, day_rental: str) -> bool:
        try:
            float(day_rental)
            return True
        except Exception:
            return False

    def user_input(self, messages: str):
        return input(messages)

    def exit_application(self, confim: str):
        if (confim == Constants.EXIT_APPLICATION):
            print("Good bye!")
            exit()
