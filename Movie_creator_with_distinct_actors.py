import json
from builder.Builder_director import DirectorBuilder
from builder.Builder_actors import ActorBuilder
from builder.Moviebuilder import MovieBuilder
import os

class Main:
 def __init__(self):

  self.actors_list = []
  self.directors_list = []
  self.movies_list = []


 def get_or_create_actor(self,name, year_of_birth, awards_count, movies_starred_in):
    for actor in self.actors_list:
        if actor.give_name() == name:
            return actor
    actor_builder = ActorBuilder()
    new_actor = (actor_builder
                 .set_name(name)
                 .set_year_of_birth(year_of_birth)
                 .set_awards_received(awards_count)
                 .set_movies_starred_in(movies_starred_in)
                 .build())
    self.actors_list.append(new_actor)
    return new_actor


 def get_or_create_director(self, name, year_of_birth, awards_count, movies_directed, years_of_directing):
    for director in self.directors_list:
        if director.give_name() == name:
            return director
    director_builder = DirectorBuilder()
    new_director = (director_builder
                    .set_name(name)
                    .set_birth_year(year_of_birth)
                    .set_awards_count(awards_count)
                    .set_movies_directed(movies_directed)
                    .set_years_of_directing(years_of_directing)
                    .build())
    self.directors_list.append(new_director)
    return new_director
 

 def run(self):
  
  path = os.path.join(os.path.dirname(__file__), 'data', 'Duomenis_Filmam.json')
  path = os.path.abspath(path)
  with open(path, 'r') as file:
    data = json.load(file)

  for movie_data in data['movies']:
    director = self.get_or_create_director(
        name=movie_data['director']['name'],
        year_of_birth=movie_data['director']['birth_year'],
        awards_count=movie_data['director']['awards_count'],
        movies_directed=movie_data['director']['movies_directed'],
        years_of_directing=movie_data['director']['years_of_directing']
    )

    actor_builders = []
    for actor_data in movie_data['actors']:
        actor = self.get_or_create_actor(
            name=actor_data['name'],
            year_of_birth=actor_data['birth_year'],
            awards_count=actor_data['awards_count'],
            movies_starred_in=actor_data['movies_starred_in']
        )
        actor_builders.append(actor)

    movie_builder = MovieBuilder()
    movie = (movie_builder
             .set_id(movie_data['id'])
             .set_title(movie_data['title'])
             .set_year(movie_data['year'])
             .set_genre(movie_data['genre'])
             .set_director(director)
             .set_plot(movie_data['plot'])
             .set_rating(movie_data['rating'])
             .set_actors(actor_builders)
             .set_price(movie_data['price'])
             .set_poster_link(movie_data['poster_link'])
             .build())

    self.movies_list.append(movie)
 

 def get_movie_list(self):
    return self.movies_list
 

 def get_actor_list(self):
    return self.actors_list
 

 def get_director_list(self):
    return self.directors_list
 
 



