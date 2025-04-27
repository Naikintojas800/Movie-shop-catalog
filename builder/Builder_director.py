from classes.Actor_and_director import Directors


class DirectorBuilder:
    def __init__(self):
        self.__name = ""
        self.__year_of_birth = 0
        self.__awards_received = 0
        self.__list_of_movies_directed = []
        self.__years_of_directing = 0

    def set_name(self, name):
        self.__name = name
        return self

    def set_birth_year(self, birth_year):
        self.__year_of_birth = birth_year
        return self

    def set_awards_count(self, awards_count):
        self.__awards_received = awards_count
        return self

    def set_movies_directed(self, movies_directed):
        self.__list_of_movies_directed = movies_directed
        return self

    def set_years_of_directing(self, years_of_directing):
        self.__years_of_directing = years_of_directing
        return self

    def build(self):
        if None in [
            self.__name, self.__year_of_birth, self.__awards_received, 
            self.__list_of_movies_directed, self.__years_of_directing
        ]:
            raise ValueError("All fields must be set before building the Director.")
        
        return Directors(
            name=self.__name,
            year_of_birth=self.__year_of_birth,
            list_of_movies_directed=self.__list_of_movies_directed,
            awards_received=self.__awards_received,
            years_of_directing=self.__years_of_directing
        )
