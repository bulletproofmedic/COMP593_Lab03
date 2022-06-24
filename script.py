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
                'title': 'Jason Bourne',
                'genre': 'Action'
            }

        ]
    }

    info['favorite_movies'].append({'title': 'John Wick', 'genre': 'action'})

# Add new toppings
    new_toppings = ('bacon', 'extra cheese')
    def add_toppings(pizza, toppings):
        info['favorite_pizza_toppings'].extend(new_toppings)
    
    add_toppings(info, new_toppings)

# Sort and uncapitalize
    def sort_uncapitalize():
            info['favorite_pizza_toppings'].sort()
            for a,t in enumerate(info['favorite_pizza_toppings']):
                info['favorite_pizza_toppings'][a] = t.lower()
            #[b] = list.sort(info['favorite_pizza_toppings'])
            #info['favorite_pizza_toppings'].pop(0)
            # I thought the sort function was adding a None object to my list so I
            # tried popping it. Then I realized that it was actually converting
            # bacon to a None object. I can't figure out why.
            return
    
    sort_uncapitalize()

    print(info['favorite_pizza_toppings'])

# Main function call
main()