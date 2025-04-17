from query import Query
from Movie_creator_with_distinct_actors import Main
from purchase import Purchase 
from fullselector import shopfront




main = Main()
main.run()

movie_list = main.get_movie_list()
actor_list = main.get_actor_list()
director_list = main.get_director_list()

query = Query(movie_list, actor_list, director_list)
Cart = Purchase(movie_list)
shop = shopfront(Cart, query)

shop.le_shop_fronte()