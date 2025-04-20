from abc import ABC


class Human(ABC): 
    def __init__(self, name, year_of_birth):
        self.__year_of_birth = year_of_birth
        self.__name = name

    def give_name(self):
        return self.__name

    def give_year_of_birth(self):
        return self.__year_of_birth


class Actors(Human):
    def __init__(self, name, year_of_birth, list_of_movies_starred_in, awards_received):
        super().__init__(name, year_of_birth)
        self.__list_of_movies_starred_in = list_of_movies_starred_in
        self.__awards_received = awards_received

    def give_list_of_movies_starred_in(self):
        return self.__list_of_movies_starred_in

    def give_awards_received(self):
        return f'{self.__awards_received} for acting'


class Directors(Human):
    def __init__(self, name, year_of_birth, list_of_movies_directed, awards_received, years_of_directing):
        super().__init__(name, year_of_birth)
        self.__list_of_movies_directed = list_of_movies_directed
        self.__awards_received = awards_received
        self.__years_of_directing = years_of_directing

    def give_list_of_movies_directed(self):
        return self.__list_of_movies_directed

    def give_awards_received(self):
        return f'{self.__awards_received} for directing'

    def give_years_of_directing(self):
        return self.__years_of_directing




