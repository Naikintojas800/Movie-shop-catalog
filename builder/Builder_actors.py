from classes.Aktoriai_ir_director import Actors


class ActorBuilder:
    def __init__(self):
        self.__name = ""
        self.__year_of_birth = 0
        self.__awards_received = 0
        self.__movies_starred_in = []

    def set_name(self, name):
        self.__name = name
        return self

    def set_year_of_birth(self, year_of_birth):
        self.__year_of_birth = year_of_birth
        return self

    def set_awards_received(self, awards_received):
        self.__awards_received = awards_received
        return self

    def set_movies_starred_in(self, movies_starred_in):
        self.__movies_starred_in = movies_starred_in
        return self

    def build(self):
        if None in [self.__name, self.__year_of_birth, self.__awards_received, self.__movies_starred_in]:
            raise ValueError("All fields must be set before building the Actor.")
        
        return Actors(
            name=self.__name,
            year_of_birth=self.__year_of_birth,
            list_of_movies_starred_in=self.__movies_starred_in,
            awards_received=self.__awards_received
        )
