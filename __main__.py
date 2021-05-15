from models.movie import Movie
from services.movie_service import MoveService
from constants.constant import Constants
from helpers import (customer_helper, movie_helper, print_helper)
from config import Config
from utils.string_utils import StringUtils


def main():
    logger = Config.logger(__name__)
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
        print("Create your new account")
        customer_helper.set_customer_values()

    if (selected_option == Constants.OPTIONS[0]):
        print("Login")
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


if __name__ == "__main__":
    main()
