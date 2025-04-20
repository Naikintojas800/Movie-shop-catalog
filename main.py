from backsend.query import Query
from Movie_creator_with_distinct_actors import Main
from backsend.purchase import Purchase 
from backsend.fullselector import shopfront
from micselaniuos.timeclass import TimeCurrent




main = Main()
main.run()

movie_list = main.get_movie_list()
actor_list = main.get_actor_list()
director_list = main.get_director_list()

Time = TimeCurrent()
query = Query(movie_list, actor_list, director_list, Time)
Cart = Purchase(movie_list, Time)
shop = shopfront(Cart, query)

shop.le_shop_fronte()

