#-----------------------------------------------------
#   Lab 3, Personal Info - COMP 593
#
#   Description:
#       Extracts info from .csv files to create new spreadsheets
#
#   Usage:
#       python script.py
#
#   Parameters:
#       Filename - Path to the .csv file
#
#   History:
#   Date        Author      Description
#   2022-06-24  A. Walker   Initial Creation
#-----------------------------------------------------

#
# #
# #
# # Come back to header to check params
# #
# #
#

# Main function definition
def main():
    
    info = {
        'full_name': 'Walker, Anthony Walker',
        'student_id': '007',
        'favorite_pizza_toppings': [
            'Soylent Green',
            'cheese',
            'hot peppers',
        ],
        'favorite_movies': [
            
            {
                'title': 'James Bond',
                'genre': 'Action'
            },
            {
                'title': 'Star Wars',
                'genre': 'Science Fiction'
            }

        ]
    }

# Add a new movie
    def new_movie():
        info['favorite_movies'].append({'title': 'Harry Potter', 'genre': 'Adventure'})
    new_movie()

# Print topping list
    def print_topping():
        print(f'My favorite pizza toppings are:')
        for topping in info['favorite_pizza_toppings']:
            print(f'- {topping}')
    #print_topping()

# Add new toppings
    new_toppings = ('bacon', 'extra cheese')
    def add_toppings(pizza, toppings):
        info['favorite_pizza_toppings'].extend(new_toppings)
    
    add_toppings(info, new_toppings)

# Sort and uncapitalize. Yes, that's a word. I just made it up.
    def sort_uncapitalize():
            for a,t in enumerate(info['favorite_pizza_toppings']):
                info['favorite_pizza_toppings'][a] = t.lower()
            
            info['favorite_pizza_toppings'].sort()
            return
    
    sort_uncapitalize()

# Print topping list again
    #print_topping()

# Print name and ID
    def name(name):
        print(f"My name is {info['full_name']} - but you can call me Agent {info['full_name'].split(',')[0]}.")
        print('My student ID is ', info['student_id'], '.', sep='')

    name(info)
    #print(info['favorite_pizza_toppings'])

# Create a list of movie genres
    def genre(type):
        list = info['favorite_movies']
        print(f"I like to watch {list[0]['genre'].lower()}, {list[1]['genre'].lower()}, and {list[2]['genre'].lower()} movies.")
    genre(info)

# Print favorite movie list
    def movies(movies_list):
        list = info['favorite_movies']
        i = 0
        print(f"Some of my favorite movies are {list[0]['title'].title()}, {list[1]['title'].title()}, and {list[2]['title'].title()}.")
    movies(info)
        
##############################
#   Attempts to iterate through list of dictionaries to make sure the function
#   could work regardless of the size of list. Failed.
#   But at least I got the Oxford comma in there!
#
##############################
#
#        for dict in list:
#            for key, value in dict:
#                print(dict[key])
#
##############################
#
#        while i <= len(list):
#            for movie.value() in list[i]:
#                movies.extend(movie)
#                print(movie)
#                i += 1
#        print(movies)
#
##############################
#
#        print ('some of my favorite movies are')
#        for movie in list:
#            print['title'].title()
#
##############################


# Main function call
main()
