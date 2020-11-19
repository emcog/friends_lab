import pdb

def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food_guess):
    persons_snacks = person["favourites"]["snacks"]
    snack_found = False # setting a flag for found
    for snack in persons_snacks: # looping through all snack/choices
        if snack == food_guess:
            snack_found = True # if at any loop a snack is found we set true
    return snack_found

def add_friend(person, friend_name):
    # find the person in the dictionary
    # open their list of friends
    # append list of freinds with friend_name
    
    person['friends'].append(friend_name)
    
def remove_friend(person, friend_name):
    # set a counter to store the index
    index = 0
    # find the person in the dictionary
    # open their list of friends
    # loop through the list of friends
    # if we find the person, store the person
    # inject index into pop to remove person
    person_friend_list = person['friends']
    for friend in person_friend_list:
        if friend == friend_name:
            person_friend_list.pop(index)
        index += 1
    
     
def total_money(people_list):
    total_monies = 0
    for person in people_list:
        # access each person's monies
        # add money to running total
        # return the total
        total_monies += person['monies']
    return total_monies

def l_money(lender, borrower, lent_amount):
    # lender
    # borrower
    # amount
    # access lender dictionary and remove lent_amount from their monies
    lender['monies'] -= lent_amount
    # access borrower dictionary and add lent_amount to their monies
    borrower['monies'] += lent_amount

def all_favourite_foods(people_list):
    # define favourite foods list
    peoples_favourite_foods = []
    # loop through each person
    for person in people_list:
        # concatenate a list entries in to one list
        peoples_favourite_foods += person['favourites']['snacks']
        # make a list of lists
        # peoples_favourite_foods.append(person['favourites']['snacks'])
    # take the list foods
    # concatenate it with running total of favourite foods
    return peoples_favourite_foods

def find_no_friendends(people_list):
    # defining an dictionary empty of people
    # looping through people_list
    # for each person check if friends_list = 0
    # if it does add to no_friends_dictionary
    # return a dictionary