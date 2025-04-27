import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.Actor_and_director import Actors, Directors

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.Movie import Movie

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from micselaniuos.timeclass import TimeCurrent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backsend.query import Query

from unittest.mock import patch

import unittest

class TestAllMoviesMethod(unittest.TestCase):

    def setUp(self):
        actor1 = Actors("Leonardo DiCaprio", 1974, ["Inception", "Titanic"], 2)
        actor2 = Actors("Kate Winslet", 1975, ["Titanic", "The Reader"], 1)
        actor3 = Actors("Matthew McConaughey", 1969, ["Interstellar", "Magic Mike"], 1)
        actor4 = Actors("Anne Hathaway", 1982, ["Interstellar", "Les Misérables"], 1)
        
        director1 = Directors("Christopher Nolan", 1970, ["Inception", "Interstellar"], 3, 20)
        director2 = Directors("James Cameron", 1954, ["Titanic", "Avatar"], 4, 30)
        
        movie1 = Movie("Inception", 1, 2010, 4, "Sci-Fi", director1, 
                            "A thief who steals corporate secrets through the use of dream-sharing technology...", 8.8, 15, 
                            "link_to_poster_inception.jpg", [actor1, actor2])
        
        movie2 = Movie("Interstellar", 2, 2014, 5, "Sci-Fi", director2, 
                            "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival...", 8.6, 18, 
                            "link_to_poster_interstellar.jpg", [actor3, actor4, actor1])
        
        time = TimeCurrent()
        actor_list = [actor1, actor2, actor3, actor4]
        director_list = [director1, director2]
        Movie_list = [movie1, movie2]
        self.query_instance = Query(Movie_list, actor_list, director_list, time)

    @patch('builtins.print')
    @patch.object(Query, 'log')
    def test_all_movies(self, mock_log, mock_print):
        self.query_instance.all_movies()
        mock_print.assert_any_call("Inception : ID - 1")
        mock_print.assert_any_call("Interstellar : ID - 2")
        self.assertGreaterEqual(mock_print.call_count, 2)  
        mock_log.assert_called_once()

    @patch('builtins.print')
    def test_movie_titles(self, mock_print):
        self.query_instance.all_movies()
        mock_print.assert_any_call("Inception : ID - 1")
        mock_print.assert_any_call("Interstellar : ID - 2")
        self.assertGreaterEqual(mock_print.call_count, 2) 
        
    
    @patch('builtins.print')
    @patch.object(Query, 'log')
    def test_all_actors(self, mock_log, mock_print):
        self.query_instance.all_actors()
        mock_print.assert_any_call("Leonardo DiCaprio")
        mock_print.assert_any_call("Kate Winslet")
        mock_print.assert_any_call("Matthew McConaughey")
        mock_print.assert_any_call("Anne Hathaway")
        self.assertGreaterEqual(mock_print.call_count, 4)  
        mock_log.assert_called_once_with(f'Function "all_actors" was called - {self.query_instance.Time.get_time()}')  


    @patch('builtins.print')
    @patch.object(Query, 'log')
    def test_all_directors(self, mock_log, mock_print):
        self.query_instance.all_directors()
        mock_print.assert_any_call("Christopher Nolan")
        mock_print.assert_any_call("James Cameron")
        self.assertGreaterEqual(mock_print.call_count, 2)
        mock_log.assert_called_once_with(f'Function "all_directors" was called - {self.query_instance.Time.get_time()}')  


    @patch('builtins.print')
    @patch.object(Query, 'log')
    def test_actor_info_found(self, mock_log, mock_print):
        self.query_instance.actor_info("Leonardo DiCaprio")
        mock_print.assert_any_call(f"{'Name:':<25} Leonardo DiCaprio")
        mock_print.assert_any_call(f"{'Year of Birth:':<25} 1974")
        mock_print.assert_any_call(f"{'Awards Received:':<25} 2")
        mock_print.assert_any_call(f"{'Movies Starred In:':<25} ['Inception', 'Titanic']")
        self.assertGreaterEqual(mock_print.call_count, 4)
        mock_log.assert_called_once_with(f'Function "actor_info" was called, using the name - "Leonardo DiCaprio" - {self.query_instance.Time.get_time()}')

    @patch('builtins.print')
    @patch.object(Query, 'log')
    def test_actor_info_not_found(self, mock_log, mock_print):
        self.query_instance.actor_info("Tom Hanks")
        mock_print.assert_any_call(f'No actors found with the name - Tom Hanks \n Check if the actor is in our database, or check if the name is written correctly')
        mock_log.assert_called_once_with(f'Function "actor_info" was called, using the name - "Tom Hanks", but was unsuccessful - {self.query_instance.Time.get_time()}')
    

    @patch('builtins.print')
    @patch.object(Query, 'log')
    def test_director_info_found(self, mock_log, mock_print):
        self.query_instance.director_info("Christopher Nolan")
        mock_print.assert_any_call(f"{'Name:':<25} Christopher Nolan")
        mock_print.assert_any_call(f"{'Year of Birth:':<25} 1970")
        mock_print.assert_any_call(f"{'Awards Received:':<25} 3")
        mock_print.assert_any_call(f"{'Years directing:':<25} 20")
        mock_print.assert_any_call(f"{'Movies directed:':<25} ['Inception', 'Interstellar']")
        self.assertGreaterEqual(mock_print.call_count, 5)
        mock_log.assert_called_once_with(f'Function "director_info" was called, using the name - "Christopher Nolan" - {self.query_instance.Time.get_time()}')

    @patch('builtins.print')
    @patch.object(Query, 'log')
    def test_director_info_not_found(self, mock_log, mock_print):
        self.query_instance.director_info("Quentin Tarantino")
        mock_print.assert_any_call(f'No directors found with the name - Quentin Tarantino \n Check if the director is in our database, or check if the name is written correctly')
        mock_log.assert_called_once_with(f'Function "director_info" was called, using the name - "Quentin Tarantino", but was unsuccessful - {self.query_instance.Time.get_time()}')


          

if __name__ == '__main__':
    unittest.main()





