class Purchase:
    def __init__(self, movie_list):
        self.name = None
        self.cost = 0
        self.choice = None
        self.cart = []
        self.__movie_list = movie_list
        self.subchoise = None
        self.id = None

    def add_to_cart(self):
            
        while True:
         print('\nWhat would you like to do?')
         print('1 - Add to cart')
         print('2 - Remove from cart')
         print('3 - View cart')
         print('4 - Purchase')
         print('5 - End interaction \n')

         self.choice = input("Select an option (1-5): ")

         if self.choice == '1':
              
              print(f'Will you use the ID or Tittle?\n')
              print(f'Id - 1 ')
              print(f'Tittle - 2 ')
              self.subchoise = input("Select an option (1-2):")
              print('\n')

              if self.subchoise == '1':
                
                  self.id = input("Enter the id of the movie you wish to buy: ")
                  found = False 
                  for movie in self.__movie_list:
                      if movie.give_id() == self.id:
                          self.cart.append(movie.give_title())
                          self.cost += movie.give_price()
                          found = True
                          break
                  if not found:
                    print(
                        f'No movie found with the name - {self.name}\n'
                        'Check if the movie is in our database, or if the name is written correctly.'
                    )
              elif self.subchoise == '2':

                 self.name = input("Enter the name of the movie you wish to buy: ")
                 found = False
                 for movie in self.__movie_list:
                    if movie.give_title() == self.name:
                        self.cart.append(movie.give_title())
                        self.cost += movie.give_price()
                        found = True
                        break
                 if not found:
                    print(
                        f'No movie found with the name - {self.name}\n'
                        'Check if the movie is in our database, or if the name is written correctly.'
                    )

         elif self.choice == '2':
            
                self.name = input("Enter the name of the movie you wish to remove from the cart: ")
                found = False
                for movie_in_list in self.cart:
                    if movie_in_list == self.name:
                        self.cart.remove(movie_in_list)

                        for movie in self.__movie_list:
                            if movie.give_title() == self.name:
                                self.cost -= movie.give_price()
                        found = True
                        break
                if not found:
                    print(
                        f'No movie found with the name - {self.name}\n'
                        'Check if the movie is in your cart or if the name is written correctly.'
                    )

         elif self.choice == '3':
                print("\nItems in your cart:")
                for item in self.cart:
                    print(f"- {item}")
                print(f'\nTotal Price: {self.cost}')

         elif self.choice == '4':
                print(f'\nThe cost of your purchase: {self.cost}')
                print('Thank you for your purchase!')
                break

         elif self.choice == '5':
                print("Goodbye!")
                break

         else:
                print("Invalid selection. Please try again.")