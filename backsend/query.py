import textwrap
from micselaniuos.decorator import me_DICAROTORer
import os


class Query:
    def __init__(self, movielist, actorlist, directorlist, Time):
        self.__movie_list = movielist
        self.__actor_list = actorlist
        self.__director_list = directorlist
        self.choise = None
        self.moviename = None
        self.Time = Time

    
    def log(self, message):
        path = 'C:\\Users\\mazut\\Desktop\\Movie-shop-catalog\\data\\logs.txt'
        log_dir = os.path.dirname(path)
        if not os.path.exists(log_dir):
         os.makedirs(log_dir)
        with open(path, 'a', encoding='utf-8') as file:
            file.write(message + '\n')

    @me_DICAROTORer
    def all_movies(self):
        for movie in self.__movie_list:
            print(f'{movie.give_title()} : ID - {movie.give_id()}')
        print('\n')    
        self.log(f'Function "all_movies" was called - {self.Time.get_time()}')

    @me_DICAROTORer
    def all_actors(self):
        for actor in self.__actor_list:
            print(actor.give_name())
        print('\n')     
        self.log(f'Function "all_actors" was called - {self.Time.get_time()}')

    @me_DICAROTORer
    def all_directors(self):
        for director in self.__director_list:
            print(director.give_name())
        print('\n')     
        self.log(f'Function "all_directors" was called - {self.Time.get_time()}')

    @me_DICAROTORer
    def actor_info(self, actor_name):
        found = False
        for actor in self.__actor_list:
            if actor.give_name() == actor_name:
                print(f"{'Name:':<25} {actor.give_name()}")
                print(f"{'Year of Birth:':<25} {actor.give_year_of_birth()}")
                print(f"{'Awards Received:':<25} {actor.give_awards_received()}")
                print(f"{'Movies Starred In:':<25} {actor.give_list_of_movies_starred_in()}")
                print('\n') 
                found = True
                self.log(f'Function "actor_info" was called, using the name - "{actor.give_name()}" - {self.Time.get_time()}')
                break

        if not found:
            print(f'No actors found with the name - {actor_name} \n Check if the actor is in our database, or check if the name is written correctly')
            self.log(f'Function "actor_info" was called, using the name - "{actor_name}", but was unsuccessful - {self.Time.get_time()}')

    @me_DICAROTORer
    def director_info(self, director_name):
        found = False
        for director in self.__director_list:
            if director.give_name() == director_name:
                print(f"{'Name:':<25} {director.give_name()}")
                print(f"{'Year of Birth:':<25} {director.give_year_of_birth()}")
                print(f"{'Awards Received:':<25} {director.give_awards_received()}")
                print(f"{'Years directing:':<25} {director.give_years_of_directing()}")
                print(f"{'Movies directed:':<25} {director.give_list_of_movies_directed()}")
                print('\n') 
                found = True
                self.log(f'Function "director_info" was called, using the name - "{director.give_name()}" - {self.Time.get_time()}')
                break

        if not found:
            print(f'No directors found with the name - {director_name} \n Check if the director is in our database, or check if the name is written correctly')
            self.log(f'Function "director_info" was called, using the name - "{director_name}", but was unsuccessful - {self.Time.get_time()}')

    @me_DICAROTORer
    def movie_info(self):
        
        print(f'Will you use the ID or Tittle?\n')
        print(f'Id - 1 ')
        print(f'Tittle - 2 ')
        self.choise = input("Select an option (1-2) : ")
        print('\n')

        if self.choise == '1':

            self.movie_id = input('Input the Id of the movie you would like to see : ')
            print('\n')

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
                print('\n') 

                found = True
                self.log(f'Function "movie_info" was called, using id - "{movie.give_id()}" - {self.Time.get_time()}')
                break

            if not found:
                print(f'No movie found with the id - {self.movie_id} \n Check if the movie is in our database, or check if the name is written correctly')
                self.log(f'Function "movie_info" was called, using the name - "{self.movie_id}", but was unsuccessful - {self.Time.get_time()}')

        elif self.choise == '2':
          
          self.movie_id = input('Input the Id of the movie you would like to see : ')
          print('\n')
          

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
                print('\n') 

                found = True
                self.log(f'Function "movie_info" was called, using the name - "{movie.give_title()}" - {self.Time.get_time()}')
                break

          if not found:
             print(f'No movie found with the name - {self.moviename} \n Check if the movie is in our database, or check if the name is written correctly')
             self.log(f'Function "movie_info" was called, using the name - "{self.moviename}", but was unsuccessful - {self.Time.get_time()}')






       