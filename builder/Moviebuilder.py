from classes.Movie import Movie


class MovieBuilder:
    def __init__(self):
        self.__title = None
        self.__movie_id = None
        self.__year = None
        self.__number_of_awards = None
        self.__genre = None
        self.__director = None
        self.__plot = None
        self.__rating = None
        self.__actors = None
        self.__price = None
        self.__poster_link = None

    def set_title(self, title):
        self.__title = title
        return self

    def set_id(self, movie_id):
        self.__movie_id = movie_id
        return self

    def set_year(self, year):
        self.__year = year
        return self

    def set_number_of_awards(self, number_of_awards):
        self.__number_of_awards = number_of_awards
        return self

    def set_genre(self, genre):
        self.__genre = genre
        return self

    def set_director(self, director):
        self.__director = director
        return self

    def set_plot(self, plot):
        self.__plot = plot
        return self

    def set_rating(self, rating):
        self.__rating = rating
        return self

    def set_actors(self, actors):
        self.__actors = actors
        return self

    def set_price(self, price):
        self.__price = price
        return self

    def set_poster_link(self, poster_link):
        self.__poster_link = poster_link
        return self

    def build(self):
        if None in [
            self.__title, self.__movie_id, self.__year, self.__genre, 
            self.__director, self.__plot, self.__rating, self.__actors, 
            self.__price, self.__poster_link
        ]:
            raise ValueError("All fields must be set before building the Movie.")
        
        return Movie(
            title=self.__title,
            movie_id=self.__movie_id,
            year=self.__year,
            number_of_awards=self.__number_of_awards,
            genre=self.__genre,
            director=self.__director,
            plot=self.__plot,
            rating=self.__rating,
            actors=self.__actors,
            price=self.__price,
            poster_link=self.__poster_link
        )
