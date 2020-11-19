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



