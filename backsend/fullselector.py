class shopfront:
    def __init__(self, purchase, query):
        self.le_choise = None
        self.purchase = purchase
        self.query = query
        self.le_smoler_choise = None
        self.serchting = None

    def le_shop_fronte(self):
    
     while True:
        
        print("*****************************************************")
        print('Hello and welcome to our shop\n')
        print('What would you like to do?')  
        print('1 - View our catalog and get info on : Movies, Actors, Directors')  
        print('2 - View your shoping cart, add to it, remove from it, and make a purchase')  
        print('3 - Leave :(')  
        print('What will it be?\n')
        self.le_choise = input('Select 1-3 : ')
        print("*****************************************************")
        print('\n')

        if self.le_choise == '1':
           
         while True:
            
            print("*****************************************************")
            print('welcome to our catalog')
            print('Here you can view our list of movies their, actors, directors and the info about said movies')
            print('Our list of movies - 1')
            print('All of the actors  - 2')
            print('All of the directors  - 3')
            print('Info about a specifict actor  - 4')
            print('Info about a specifict director  - 5')
            print('Info about a specifict movie  - 6')
            print('Exit - 7')
            print('What will it be?')
            self.le_smoler_choise = input('Select 1-7 : ')
            print("*****************************************************")
            print('\n')

            if self.le_smoler_choise == '1':
                self.query.all_movies()

            elif self.le_smoler_choise == '2':
               self.query.all_actors()

            elif self.le_smoler_choise == '3':
               self.query.all_directors()

            elif self.le_smoler_choise == '4':
               self.serchting = input('Select the name of actor : ')
               self.query.actor_info(self.serchting)   

            elif self.le_smoler_choise == '5':
               self.serchting = input('Select the name of director : ')
               self.query.director_info(self.serchting) 

            elif self.le_smoler_choise == '6':
               self.query.movie_info()   

            elif self.le_smoler_choise == '7':
               break

            else:
               print('wrong input, try again')         

        elif self.le_choise == '2':
            
            self.purchase.add_to_cart()

        elif self.le_choise == '3':
           
           print(f'Its sad to see you gom goodbye and see you soon we hope') 
           break
        
        else:
           print('Try again wrong input')    


           
           



           