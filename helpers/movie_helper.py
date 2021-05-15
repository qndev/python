from constants.constant import Constants


def slice_string(movies: list) -> list:
    sliced = []
    for movie in movies:
        name = movie.get_name()
        category = movie.get_category().get_name()
        release_month = movie.get_release_month()
        price = movie.get_category().get_price()
        if (len(name) >= Constants.MOVIE_SCREEN_DISPLAY[0]):
            name = name[Constants.INDEX:Constants.MOVIE_SCREEN_DISPLAY[0] - 3] + "..."
        else:
            name = name + " " * \
                (Constants.MOVIE_SCREEN_DISPLAY[0] - len(name))
        if (len(category) >= Constants.MOVIE_SCREEN_DISPLAY[1]):
            category = category[Constants.INDEX:
                                Constants.MOVIE_SCREEN_DISPLAY[1] - 3] + "..."
        else:
            category = category + " " * \
                (Constants.MOVIE_SCREEN_DISPLAY[1] - len(category))
        if (len(release_month) >= Constants.MOVIE_SCREEN_DISPLAY[2]):
            release_month = release_month[Constants.INDEX:
                                          Constants.MOVIE_SCREEN_DISPLAY[2] - 3] + "..."
        else:
            release_month = release_month + " " * \
                (Constants.MOVIE_SCREEN_DISPLAY[2] - len(release_month))
        if (len(price) < Constants.MOVIE_SCREEN_DISPLAY[3]):
            price = price + " " * \
                (Constants.MOVIE_SCREEN_DISPLAY[3] - len(price))
        movie.set_name(name)
        movie.get_category().set_name(category)
        movie.set_release_month(release_month)
        movie.get_category().set_price(price)
        sliced.append(movie)
    return sliced
