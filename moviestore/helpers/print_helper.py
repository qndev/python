from typing import Dict, List, Union
from moviestore.constants.constant import Constants
from moviestore.models.invoice import Invoice
from moviestore.models.customer import Customer
from moviestore.models.movie import Movie


def print_header():
    print("++=========================================================================================================================++")
    print("||                                                                                                                         ||")
    print("||                                                      /\     /\                                                          ||")
    print("||                                                     /  \   /  \                                                         ||")
    print("||                                                    / /\ \_/ /\ \                                                        ||")
    print("||                                                   / /  \   /  \ \   QNDEV                                               ||")
    print("||                                                  /_/    \_/    \_\OVIE STORE                                            ||")
    print("||                                                                                                                         ||")
    print("++=========================================================================================================================++")


def print_options():
    print("||                                              Please select one of these options                                         ||")
    print("++=========================================================================================================================++")
    print("||                                                                                                                         ||")
    print("||                                              1. If you already have an account                                          ||")
    print("||                                              2. If you don't have an account                                            ||")
    print("||                                              3. Exit application                                                        ||")
    print("||                                                                                                                         ||")
    print("++=========================================================================================================================++")


def print_movies_options():
    print("||                                                                                                                         ||")
    print("||                                              1. View list movies                                                        ||")
    print("||                                              2. Your order invoices                                                     ||")
    print("||                                                                                                                         ||")
    print("++=========================================================================================================================++")


def print_movie_banner():
    print("+---------------------------------------------------------------------------------------------------------------------+")
    print("|                                                   List movies                                                       |")
    print("+--------------------+-----------------------------+------------------------+--------------------+--------------------+")
    print("| Movie ID           | Movie                       | Category               | Release month      | Price              |")
    print("+--------------------+-----------------------------+------------------------+--------------------+--------------------+")

# 3, 27, 22, 18, 11


def print_list_movies(movie: Movie, no: int):
    print(f"| {no}.{movie.get_movie_id()}| {movie.get_name()}| {movie.get_category().get_name()}| {movie.get_release_month()}| {movie.get_category().get_price()}|")
    print("+--------------------+-----------------------------+------------------------+--------------------+--------------------+")


def print_invoice_header_table():
    print("|-----|------------------------------|-------------------------|-------------|-------------|--------|-----------|-----------|")
    print("|No   |Movie                         |Category                 |Release month|Day of rental|Price   |Surcharge 1|Surcharge 2|")
    print("|-----|------------------------------|-------------------------|-------------|-------------|--------|-----------|-----------|")


def print_invoices(customer: dict, invoices: Union[List[Invoice], List[List[Invoice]]]):

    print_header()
    print("\nCustomer:           " + customer["name"])
    print("Customer points:    " +
          str(customer["discount_points"]) + " pts" + "\n\n")
    if (isinstance(invoices[0], Invoice)):
        print_invoice(invoices)
    else:
        for invoice in invoices:
            print_invoice(invoice)


def print_invoice(invoices: List[Invoice]):
    print("Order ID: " + invoices[0].get_order_id() +
          "   Date: " + invoices[len(invoices) - 1].get_order_date())
    table_data = []
    column_titles = ["No", "Movie", "Category", "Release month",
                     "Day of rental", "Price", "Surcharge 1", "Surcharge 2"]
    table_border = []
    # default length of column titles
    column_sizes = [2, 5, 7, 13, 13, 5, 11, 11]
    total_pay_index = len(invoices) - 1
    discount_index = total_pay_index
    index = 0
    for invoice in invoices:
        no = (index + 1)
        movie_name = invoice.get_movie_name()
        category = invoice.get_category()
        release_month = str(invoice.get_release_month())
        days_rental = str(invoice.get_days_rental())
        price = str(invoice.get_price())
        surcharge_new_movie = str(invoice.get_surcharge_new_movie())
        surcharge_days = str(invoice.get_surcharge_days())
        if (len(str(no)) > column_sizes[0]):
            column_sizes[0] = len(str(no))
        if (len(movie_name) > column_sizes[1]):
            column_sizes[1] = len(movie_name)
        if (len(category) > column_sizes[2]):
            column_sizes[2] = len(category)
        if (len(release_month) > column_sizes[3]):
            column_sizes[3] = len(release_month)
        if (len(days_rental) > column_sizes[4]):
            column_sizes[4] = len(days_rental)
        if (len(price) > column_sizes[5]):
            column_sizes[5] = len(price)
        if (len(surcharge_new_movie) > column_sizes[6]):
            column_sizes[6] = len(surcharge_new_movie)
        if (len(surcharge_days) > column_sizes[7]):
            column_sizes[7] = len(surcharge_days)
        row_data = [
            no,
            movie_name,
            category,
            release_month,
            days_rental,
            price,
            surcharge_new_movie,
            surcharge_days
        ]
        table_data.append(row_data)
        index += 1
    table_border = ["-"*column_sizes[0], "-"*column_sizes[1], "-"*column_sizes[2], "-"*column_sizes[3],
                    "-"*column_sizes[4], "-"*column_sizes[5], "-"*column_sizes[6], "-"*column_sizes[7]]
    table_data.insert(0, table_border)
    table_data.insert(1, column_titles)
    table_data.insert(2, table_border)
    table_data.append(table_border)
    seperator_table = len(invoices) + 3

    for data_raw in table_data:
        print(
            f"|{data_raw[0]:<{column_sizes[0]}}|{data_raw[1]:<{column_sizes[1]}}|{data_raw[2]:<{column_sizes[2]}}|{data_raw[3]:<{column_sizes[3]}}|{data_raw[4]:<{column_sizes[4]}}|{data_raw[5]:<{column_sizes[5]}}|{data_raw[6]:<{column_sizes[6]}}|{data_raw[7]:<{column_sizes[7]}}|")

    print("\nDiscount: " +
          str(invoices[discount_index].get_discount()) + "%")
    print(
        str("Total: " + str(invoices[total_pay_index].get_total_pay())) + "$")

    print(
        f"-{table_data[seperator_table][0]:<{column_sizes[0]}}-{table_data[seperator_table][1]:<{column_sizes[1]}}-{table_data[seperator_table][2]:<{column_sizes[2]}}-{table_data[seperator_table][3]:<{column_sizes[3]}}-{table_data[seperator_table][4]:<{column_sizes[4]}}-{table_data[seperator_table][5]:<{column_sizes[5]}}-{table_data[seperator_table][6]:<{column_sizes[6]}}-{table_data[seperator_table][7]:<{column_sizes[7]}}-" + "\n\n")
