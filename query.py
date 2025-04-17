from Movie_creator_with_distinct_actors import Main
from datetime import datetime
import textwrap


class TimeCurrent:
    def get_time(self):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_datetime

Time = TimeCurrent()

class Query:
    def __init__(self, movielist, actorlist, directorlist):
        self.__movie_list = movielist
        self.__actor_list = actorlist
        self.__director_list = directorlist
        self.choise = None
        self.moviename = None


    def log(self, message):
        with open('logs.txt', 'a', encoding='utf-8') as file:
            file.write(message + '\n')


    def all_movies(self):
        for movie in self.__movie_list:
            print(f'{movie.give_title()} : ID - {movie.give_id()}')
        self.log(f'Function "all_movies" was called - {Time.get_time()}')


    def all_actors(self):
        for actor in self.__actor_list:
            print(actor.give_name())
        self.log(f'Function "all_actors" was called - {Time.get_time()}')


    def all_directors(self):
        for director in self.__director_list:
            print(director.give_name())
        self.log(f'Function "all_directors" was called - {Time.get_time()}')


    def actor_info(self, actor_name):
        found = False
        for actor in self.__actor_list:
            if actor.give_name() == actor_name:
                print(f"{'Name:':<25} {actor.give_name()}")
                print(f"{'Year of Birth:':<25} {actor.give_year_of_birth()}")
                print(f"{'Awards Received:':<25} {actor.give_awards_received()}")
                print(f"{'Movies Starred In:':<25} {actor.give_list_of_movies_starred_in()}")
                found = True
                self.log(f'Function "actor_info" was called, using the name - "{actor.give_name()}" - {Time.get_time()}')
                break

        if not found:
            print(f'No actors found with the name - {actor_name} \n Check if the actor is in our database, or check if the name is written correctly')
            self.log(f'Function "actor_info" was called, using the name - "{actor_name}", but was unsuccessful - {Time.get_time()}')


    def director_info(self, director_name):
        found = False
        for director in self.__director_list:
            if director.give_name() == director_name:
                print(f"{'Name:':<25} {director.give_name()}")
                print(f"{'Year of Birth:':<25} {director.give_year_of_birth()}")
                print(f"{'Awards Received:':<25} {director.give_awards_received()}")
                print(f"{'Years directing:':<25} {director.give_years_of_directing()}")
                print(f"{'Movies directed:':<25} {director.give_list_of_movies_starred_in()}")
                found = True
                self.log(f'Function "director_info" was called, using the name - "{director.give_name()}" - {Time.get_time()}')
                break

        if not found:
            print(f'No directors found with the name - {director_name} \n Check if the director is in our database, or check if the name is written correctly')
            self.log(f'Function "director_info" was called, using the name - "{director_name}", but was unsuccessful - {Time.get_time()}')


    def movie_info(self):
        
        print(f'Will you use the ID or Tittle?\n')
        print(f'Id - 1 ')
        print(f'Tittle - 2 ')
        self.choise = input("Select an option (1-2):")
        print('\n')

        if self.choise == '1':

            self.movie_id = input('Input the Id of the movie you would like to see\n')

            found = False
            for movie in self.__movie_list:
              if movie.give_id() == self.movie_id:
                print(f"{'Title:':<25} {movie.give_title()}")
                print(f"{'ID:':<25} {movie.give_id()}")
                print(f"{'Year of release:':<25} {movie.give_year()}")
                print(f"{'Awards received:':<25} {movie.give_number_of_awards()}")
                print(f"{'Genre:':<25} {movie.give_genre()}")

                

                plot_text = movie.give_plot()
                width = 80

                print(f"{'Plot:':<25}", end=' ')
                wrapped_plot = textwrap.fill(plot_text, width=width)

                first_line = True
                for line in wrapped_plot.split('\n'):
                 if first_line:
                   print(line)
                   first_line = False
                 else:
                   print(f"{'':<26}{line}")


                print(f"{'Rating:':<25} {movie.give_rating()}")
                print(f"{'Price:':<25} {movie.give_price()}")
                print(f"{'Director:':<25} {(movie.give_director()).give_name()}")

                print(f"{'Actors:':<25}", end=' ')
                actor_names = ""
                for index, actor in enumerate(movie.give_actors()):
                    if index > 0:
                        actor_names += ", "
                    actor_names += actor.give_name()
                print(actor_names)

                found = True
                self.log(f'Function "movie_info" was called, using id - "{movie.give_id()}" - {Time.get_time()}')
                break

            if not found:
                print(f'No movie found with the id - {self.movie_id} \n Check if the movie is in our database, or check if the name is written correctly')
                self.log(f'Function "movie_info" was called, using the name - "{self.movie_id}", but was unsuccessful - {Time.get_time()}')

        elif self.choise == '2':
          
          self.movie_id = input('Input the Id of the movie you would like to see\n')
          

          found = False
          for movie in self.__movie_list:
            if movie.give_title() == self.moviename:
                print(f"{'Title:':<25} {movie.give_title()}")
                print(f"{'ID:':<25} {movie.give_id()}")
                print(f"{'Year of release:':<25} {movie.give_year()}")
                print(f"{'Awards received:':<25} {movie.give_number_of_awards()}")
                print(f"{'Genre:':<25} {movie.give_genre()}")

                

                plot_text = movie.give_plot()
                width = 80

                print(f"{'Plot:':<25}", end=' ')
                wrapped_plot = textwrap.fill(plot_text, width=width)

                first_line = True
                for line in wrapped_plot.split('\n'):
                 if first_line:
                   print(line)
                   first_line = False
                 else:
                   print(f"{'':<26}{line}")


                print(f"{'Rating:':<25} {movie.give_rating()}")
                print(f"{'Price:':<25} {movie.give_price()}")
                print(f"{'Director:':<25} {(movie.give_director()).give_name()}")

                print(f"{'Actors:':<25}", end=' ')
                actor_names = ""
                for index, actor in enumerate(movie.give_actors()):
                    if index > 0:
                        actor_names += ", "
                    actor_names += actor.give_name()
                print(actor_names)

                found = True
                self.log(f'Function "movie_info" was called, using the name - "{movie.give_title()}" - {Time.get_time()}')
                break

          if not found:
             print(f'No movie found with the name - {self.moviename} \n Check if the movie is in our database, or check if the name is written correctly')
             self.log(f'Function "movie_info" was called, using the name - "{self.moviename}", but was unsuccessful - {Time.get_time()}')






       