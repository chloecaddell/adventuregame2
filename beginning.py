from player_classes import *
from magical_forest import magical_forest
import sys
import os
sys.path.append(os.path.abspath(os.path.join('../', 'config')))


def beginning(user):
    character = user.character
    username = user.username
    stamina_check = user.stamina_check
    while (True):
        start = input(
            "Would you like to head to Town or The Magical Forest? Choose 'TOWN' OR 'MAGICAL FOREST': ")
        start = start.lower()
        print("\n")
        if start == "town":
            if character == cat_rogue or character == cow_barbarian:
                print(username, "the", character,
                      "walked straight through town to The Magical Forest")
                stamina_check()
                magical_forest(user)
                break
            elif character == corgi_cleric or character == frog_wizard:
                user.stamina -= 1
                if character == corgi_cleric:
                    print("You were captured by a family. Lose 1 stamina.")
                    stamina_check()
                    continue
                elif character == frog_wizard:
                    print("You were trampled. Lose 1 stamina.")
                    stamina_check()
                    continue
        if start == "the magical forest" or start == "magical forest":
            stamina_check()
            magical_forest(user)
            break
        else:
            continue
