from moviestore.models.movie import Movie
from moviestore.models.category import Category
from moviestore.utils.file_utils import FileUltils
from moviestore.constants.constant import Constants


class MoveService:
    def select_movies(self) -> list:
        movies_data, categories_data = FileUltils.read_movies_data()
        movies = []

        if bool(movies_data) & bool(categories_data):
            for movie_data in movies_data:
                movie = Movie(None, None, None, None, None)
                movie.set_movie_id(movie_data)
                movie.set_name(
                    movies_data[movie.get_movie_id()][Constants.MOVIE_KEYS[0]])
                movie.set_category_id(
                    movies_data[movie.get_movie_id()][Constants.MOVIE_KEYS[1]])
                movie.set_release_month(
                    movies_data[movie.get_movie_id()][Constants.MOVIE_KEYS[2]])

                category = Category(None, None, None, None)
                category.set_cate_id(movie.get_category_id())
                category.set_name(
                    categories_data[category.get_cateid()][Constants.CATEGORY_KEYS[0]])
                category.set_price(
                    categories_data[category.get_cateid()][Constants.CATEGORY_KEYS[1]])
                category.set_description(
                    categories_data[category.get_cateid()][Constants.CATEGORY_KEYS[2]])
                movie.set_category(category)

                movies.append(movie)

        return movies
