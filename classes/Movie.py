class Movie:
    def __init__(self, title, movie_id, year, number_of_awards, genre, director, plot, rating, actors, price, poster_link):
        self.__movie_id = movie_id
        self.__number_of_awards = number_of_awards
        self.__title = title
        self.__year = year
        self.__genre = genre
        self.__director = director
        self.__plot = plot
        self.__rating = rating
        self.__actors = actors
        self.__price = price
        self.__poster_link = poster_link

    def give_id(self):
        return self.__movie_id

    def give_title(self):
        return self.__title

    def give_year(self):
        return self.__year

    def give_number_of_awards(self):
        return self.__number_of_awards

    def give_genre(self):
        return self.__genre

    def give_plot(self):
        return self.__plot

    def give_rating(self):
        return self.__rating

    def give_price(self):
        return float(self.__price)

    def give_poster_link(self):
        return self.__poster_link

    def give_director(self):
        return self.__director

    def give_actors(self):
        return self.__actors

    