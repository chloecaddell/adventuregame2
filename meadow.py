from player_info import *
from player_classes import *
from fork import *

def meadow(user):
    character = user.character
    username = user.username
    stamina_check = user.stamina_check
    while (True):
        print(username + "," +
              " You've arrived at a small flowery meadow. A little oasis within the forest.")
        meadow_choice = input(
            "Would you like to 'PICK FLOWERS', take a 'NAP', or move further into the 'FOREST'? Choose PICK FLOWERS OR NAP OR FOREST: ")
        meadow_choice = meadow_choice.lower()
        print("\n")
        if meadow_choice == "pick flowers":
            user.stamina -= 2
            print(
                "The flowers were actually Pikmin! You started a battle, lose 2 stamina.")
            stamina_check()
            fork(user)
            break
        elif meadow_choice == "nap":
            user.stamina += 2
            print("The nap has you feeling rested. Gain 2 stamina.")
            stamina_check()
            fork(user)
            break
        elif meadow_choice == "forest":
            stamina_check()
            fork(user)
            break
        else:
            continue