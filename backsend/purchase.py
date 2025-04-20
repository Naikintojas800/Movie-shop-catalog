import os
class Purchase:
    def __init__(self, movie_list, Time):
        self.name = None
        self.cost = 0
        self.choice = None
        self.cart = []
        self.__movie_list = movie_list
        self.subchoise = None
        self.id = None
        self.time = Time
        self.objectprice = 0


    def log(self, message):
        path = 'C:\\Users\\mazut\\Desktop\\Movie-shop-catalog\\data\\logs.txt'
        log_dir = os.path.dirname(path)
        if not os.path.exists(log_dir):
         os.makedirs(log_dir)
        with open(path, 'a', encoding='utf-8') as file:
            file.write(message + '\n')


    
    def add_to_cart(self):
            
        while True:
         print("*****************************************************")
         print('welcome to your shopping cart')
         print('Here you can view your shopping cart, add or remove from it, or make a purchase')
         print('\nWhat would you like to do?')
         print('1 - Add to cart')
         print('2 - Remove from cart')
         print('3 - View cart')
         print('4 - Purchase')
         print('5 - End interaction \n')

         self.choice = input("Select an option (1-5) : ")
         print("*****************************************************")

         if self.choice == '1':
              
              print(f'Will you use the ID or Tittle?\n')
              print(f'Id - 1 ')
              print(f'Tittle - 2 ')
              self.subchoise = input("Select an option (1-2) : ")
              print('\n')

              if self.subchoise == '1':
                
                  self.id = input("Enter the id of the movie you wish to buy : ")
                  found = False 
                  for movie in self.__movie_list:
                      if movie.give_id() == self.id:
                          self.cart.append(movie.give_title())
                          self.objectprice = movie.give_price()
                          self.cost += movie.give_price()
                          found = True
                          self.log(f'Function "Add to cart" was used using id {self.id}, adding {self.objectprice} to purchase - {self.time.get_time()}')

                          break
                  if not found:
                    print(
                        f'No movie found with the name - {self.name}\n'
                        'Check if the movie is in our database, or if the name is written correctly.'
                    )
                    self.log(f'Function "Add to cart" was used using id {self.id}, but no such movie was found - {self.time.get_time()}')

              elif self.subchoise == '2':

                 self.name = input("Enter the name of the movie you wish to buy : ")
                 found = False
                 for movie in self.__movie_list:
                    if movie.give_title() == self.name:
                        self.cart.append(movie.give_title())
                        self.objectprice = movie.give_price()
                        self.cost += movie.give_price()
                        found = True
                        self.log(f'Function "Add to cart" was used using tittle {self.name}, adding {self.objectprice} to purchase - {self.time.get_time()}')
                        break
                 if not found:
                    print(
                        f'No movie found with the name - {self.name}\n'
                        'Check if the movie is in our database, or if the name is written correctly.'
                    )
                    self.log(f'Function "Add to cart" was used using tittle {self.name}, but was not found - {self.time.get_time()}')

         elif self.choice == '2':
            
                self.name = input("Enter the name of the movie you wish to remove from the cart : ")
                found = False
                for movie_in_list in self.cart:
                    if movie_in_list == self.name:
                        self.cart.remove(movie_in_list)

                        for movie in self.__movie_list:
                            if movie.give_title() == self.name:
                                self.cost -= movie.give_price()
                        found = True
                        self.log(f'Function "Remove From cart" was used using tittle {self.name}, removing {self.objectprice} to purchase - {self.time.get_time()}')
                        break
                if not found:
                    print(
                        f'No movie found with the name - {self.name}\n'
                        'Check if the movie is in your cart or if the name is written correctly.'
                    )
                    self.log(f'Function "Remove from cart" was used using tittle {self.name}, but no such movie was found in cart - {self.time.get_time()}')

         elif self.choice == '3':
                print("\nItems in your cart:")
                for item in self.cart:
                    print(f"- {item}")
                print(f'\nTotal Price: {self.cost}')
                self.log(f'Function "Show cart" was used - {self.time.get_time()}')

         elif self.choice == '4':
                print(f'\nThe cost of your purchase: {self.cost}')
                print('Thank you for your purchase!')
                self.log(f'Function "Purchase" was used for the price of {self.cost}- {self.time.get_time()}')
                print('\n')
                self.cost = 0
                self.cart = []
                break

         elif self.choice == '5':
                print('\n')
                break

         else:
                print("Invalid selection. Please try again.")
                self.log(f'Invalid selection in purchase sector - {self.time.get_time()}')