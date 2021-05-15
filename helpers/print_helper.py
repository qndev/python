from models.movie import Movie
from constants.constant import Constants


def print_header():
    print("||===============================================================================================||")
    print("||                                                                                               ||")
    print("||                                      /\     /\                                                ||")
    print("||                                     /  \   /  \                                               ||")
    print("||                                    / /\ \_/ /\ \                                              ||")
    print("||                                   / /  \   /  \ \  USOL-VN                                    ||")
    print("||                                  /_/    \_/    \_\OVIE STORE                                  ||")
    print("||                                                                                               ||")
    print("||===============================================================================================||")


def print_options():
    print("||                              Please select one of these options                               ||")
    print("||===============================================================================================||")
    print("||                                                                                               ||")
    print("||                              1. If you already have an account                                ||")
    print("||                              2. If you don't have an account                                  ||")
    print("||                                                                                               ||")
    print("||===============================================================================================||")


def print_movie_banner():
    print("||                                      List movies                                              ||")
    print("||===============================================================================================||")
    print("|| Movie                       | Category               | Release month      | Price             ||")
    print("||=============================*========================*====================*===================||")

# 3, 27, 22, 18, 11


def print_list_movies(movie: Movie, no: int):
    print(f"|| {no}.{movie.get_name()}| {movie.get_category().get_name()}| {movie.get_release_month()}| {movie.get_category().get_price()} ||")
