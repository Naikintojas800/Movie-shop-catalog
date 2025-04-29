# REPORT

* Introduction
  * a. My application is a Movie shop catalog
  * b. You need to run the main.py file
  * c. You use the program by inputting numbers according to the selection given, copy and pasting names when needed
* Body/Analysis  
  * Polymorphism/inheritance/abstraction/encapsulation  
    
    They are implemented in this class alone:  
    Abstraction is used in the human class it serves as the basis for the Actor ar Director classes  
    Inheritance is used to create the Actor and Director classes from the Human class wich in this case is the father class
    Polymorphism is used in the method 'Give_awards_received'  
    Encapsulation is used in all 3 classes as all variables are previte and the only way to get them is by using methods  
    

    ```python
    from abc import ABC

    class Human(ABC): 
        def __init__(self, name, year_of_birth):
            self.__year_of_birth = year_of_birth
            self.__name = name

        def give_name(self):
            return self.__name

        def give_year_of_birth(self):
            return self.__year_of_birth


    class Actors(Human):
        def __init__(self, name, year_of_birth, list_of_movies_starred_in, awards_received):
            super().__init__(name, year_of_birth)
            self.__list_of_movies_starred_in = list_of_movies_starred_in
            self.__awards_received = awards_received

        def give_list_of_movies_starred_in(self):
            return self.__list_of_movies_starred_in

        def give_awards_received(self):
            return f'{self.__awards_received} for acting'


    class Directors(Human):
        def __init__(self, name, year_of_birth, list_of_movies_directed, awards_received, years_of_directing):
            super().__init__(name, year_of_birth)
            self.__list_of_movies_directed = list_of_movies_directed
            self.__awards_received = awards_received
            self.__years_of_directing = years_of_directing

        def give_list_of_movies_directed(self):
            return self.__list_of_movies_directed

        def give_awards_received(self):
            return f'{self.__awards_received} for directing'

        def give_years_of_directing(self):
            return self.__years_of_directing
    ```

  * Two design patterns were used:  
   **Builder**

    ```python
    from classes.Aktoriai_ir_director import Actors

    class ActorBuilder:
        def __init__(self):
            self.__name = ""
            self.__year_of_birth = 0
            self.__awards_received = 0
            self.__movies_starred_in = []

        def set_name(self, name):
            self.__name = name
            return self

        def set_year_of_birth(self, year_of_birth):
            self.__year_of_birth = year_of_birth
            return self

        def set_awards_received(self, awards_received):
            self.__awards_received = awards_received
            return self

        def set_movies_starred_in(self, movies_starred_in):
            self.__movies_starred_in = movies_starred_in
            return self

        def build(self):
            if None in [self.__name, self.__year_of_birth, self.__awards_received, self.__movies_starred_in]:
                raise ValueError("All fields must be set before building the Actor.")
            
            return Actors(
                name=self.__name,
                year_of_birth=self.__year_of_birth,
                list_of_movies_starred_in=self.__movies_starred_in,
                awards_received=self.__awards_received
            )
       ```
    **Decorator**
     ```python
     def me_DICAROTORer(func):
       def wrapper(*args, **kwargs):
        print("*****************************************************")
        result = func(*args, **kwargs)
        print("*****************************************************")
        return result
       return wrapper
     ```
   * Agregation was used
     Here is a movie class whitout it's methods  
     For it to be crated it needs multiple independant objects (actors/director)  
     The actor and director classes were presented previously   
     ```python
     class Movie:
      def __init__(self, title, movie_id, year, number_of_awards, genre, director, plot, rating, actors, price, poster_link):
        self.__movie_id = movie_id
        self.__number_of_awards = number_of_awards
        self.__title = title
        self.__year = year
        self.__genre = genre
        self.__director = director
        self.__plot = plot
        self.__rating = rating
        self.__actors = actors
        self.__price = price
        self.__poster_link = poster_link
     ```
  * The program both read and writes from/into files

    **To create the needed objects it reads the data from a json file**  
    Example data for 1 movie
    ```json
    "movies": [
    {
      "id": "1",
      "title": "Inception",
      "year": 2010,
      "genre": "Sci-Fi",
      "director": {
        "name": "Christopher Nolan",
        "birth_year": 1970,
        "awards_count": 15,
        "movies_directed": ["Inception", "500 Days of Summer", "Looper", "The Dark Knight Rises"],
        "years_of_directing": 33
      },
      "plot": "A skilled thief is given a chance to have his criminal record erased if he can successfully perform an inception: planting an idea into the mind of a CEO.",
      "rating": 8.8,
      "actors": [
        {
          "name": "Leonardo DiCaprio",
          "birth_year": 1974,
          "awards_count": 23,
          "movies_starred_in": ["Inception", "The Wolf of Wall Street", "Titanic", "Shutter Island"]
        },
        {
          "name": "Joseph Gordon-Levitt",
          "birth_year": 1981,
          "awards_count": 5,
          "movies_starred_in": ["Inception", "500 Days of Summer", "Looper", "The Dark Knight Rises"]
        },
        {
          "name": "Ellen Page",
          "birth_year": 1987,
          "awards_count": 1,
          "movies_starred_in": ["Inception", "Juno", "Hard Candy", "Whip It"]
        }
      ],
      "price": 19.99,
      "poster_link": "https://linktotheposter.com/inception.jpg"
    }
    ```
    **During it's use the program logs the interactions**  
    Exmample for 1 log
    ```txt
    Function "Add to cart" was used using id 1, adding 19.99 to purchase - 2025-04-18 09:03:20
    ```
* Results and Summary
  * **Results**  
    * The end product is a functional program that emulatates the shopping experiece of a phisical shop (like BLOCKBUSTER)
    * During the production of of the main hurdles was writing the tests
    * The program successfully utilizes the JSON data to create the necessary objects for its function.
  * **Conclusion**  
    During the production, I deepened my understanding of Python and its libraries.
I learned how to read and write data to/from files, and how to utilize different libraries to achieve different results.
As a final result, I created a program that emulates a physical shopping experience.
My program could be used as a basic shopfront for online or game-like shops, but it would require further refinement.

  * **How it would be possible to extend your application?**  
   It would probably be done through the shopfront/purchase/query files, as they are the ones that utilize the objects and use their data.
So, it would likely require the addition of new methods that implement new utilizations of the previously mentioned data.
  
    
    
     

    
