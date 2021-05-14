class Movie:
    def __init__(self, movie_id = None, name = None, release_month = None, category_id = None):
        self._movie_id = movie_id
        self._name = name
        self._release_month = release_month
        self._category_id = category_id

    def get_movie_id(self):
        return self._movie_id

    def set_movie_id(self, movie_id):
        self._movie_id = movie_id
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    
    def get_release_month(self):
        return self._release_month

    def set_release_month(self, release_month):
        self._release_month = release_month

    def get_category_id(self):
        return self._category_id

    def set_category_id(self, category_id):
        self._category_id = category_id
