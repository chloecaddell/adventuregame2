from player_info import *
from player_classes import *
from pond_cave import *

def magical_forest(user):
    character = user.character
    username = user
    stamina_check = user.stamina_check
    while (True):
        print("Welcome to The Magical Forest.")
        mushroom = input(
            "You have run into Mushroom People. Would you like to challenge them to a dance battle or sneak around them? Choose 'DANCE' OR 'SNEAK': ")
        mushroom = mushroom.lower()
        print("\n")
        if mushroom == "dance":
            print("The dance off has cost you 1 stamina.")
            user.stamina -= 1
            stamina_check()
            pond_cave(user)
            break
        elif mushroom == "sneak":
            stamina_check()
            pond_cave(user)
            break
        else:
            continue