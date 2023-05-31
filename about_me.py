"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        # TODO: Put full name into data structure
        'name': "Akhil Mehra",
        
    
        # TODO: Put student ID into data structure
        'student ID': '10286737',
        # TODO: Put list of 3 pizza toppings into data structure
        'pizza toppings': [
                'Pepperoni',
                'Sausage',
                 'Bacon'
        ],
    
        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': 'Dune',
                'genre': 'sci-fi'
            },
            # TODO: Add one more movie
            {
          'title': 'Dog',
          'genre': 'comedy'
            }
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['Black Olives', 'Pineapple'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'Eternals', 'fantasy')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    # Print sentence containing student ID
   
    name = 'Akhil Mehra'
    first_name =name.split()[0]

    

    print(f"My name is {my_info['name']}, but you can call me Sir {first_name}.")
    print(f"My student ID is {my_info['student ID']}.")
    print()


def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    # Print bullet list of favourite pizza toppings
    print()
    print(f"My favourite pizza toppings are:")
    for pizza_toppings in my_info['pizza toppings']:

     print(f'- {pizza_toppings}')
    print()
        
        
    
def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list 
    my_info['pizza toppings'].extend(toppings)

    # Convert all pizza toppings to lowercase
    for i, pizza_toppings in enumerate(my_info['pizza toppings']):
        my_info['pizza toppings'][i] = pizza_toppings.lower()
        
    
    # Sort toppings list alphabetically
    my_info['pizza toppings'].sort()
    return


def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    my_info['movies'].append({'title':title, 'genre': genre})
    return


def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7 

    genres = [movie['genre'] for movie in my_info['movies']]
    genres_list = ', '.join(genres) 
    print(f"I like to watch {genres_list} movies.")
    print()
    

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    titles = [movie['title'] for movie in movie_list]
    title_list = ', '.join(titles)
   
    print(f"Some of my favourite movies are {title_list}!")

if __name__ == '__main__':
    main()