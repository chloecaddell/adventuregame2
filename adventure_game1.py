import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'config')))
from player_info import Player
from player_classes import *
from beginning import beginning


while (True):
    print("Welcome to the mystical magical adventure game!")
    print("1) Frog Wizard")
    print("2) Cow Barbarian")
    print("3) Corgi Cleric")
    print("4) Cat Rogue")
    character = input("Choose a character: ")
    character = int(character)
    username = input("Create a character name: ").title()
    print("\n" + "The goal of this game is to get through the forest and find the Fairy Village without running out of stamina. All characters start with 5 stamina, and based on your character, different choices have different effects on your stamina. Running out of stamina can cause you to go back a round or restart depending on how far through you are.")
    if character == 1:
        character = frog_wizard
        print("The Frog is intelligent, but fragile.")
        break
    elif character == 2:
        character = cow_barbarian
        print("The Cow is strong, but reckless.")
        break
    elif character == 3:
        character = corgi_cleric
        print("The Corgi is lucky, but weak.")
        break
    elif character == 4:
        character = cat_rogue
        print("The Cat is sneaky, but dense.")
        break
    else:
        continue
user = Player(character, username)
print("You have chosen The", user.character)
print("Your name is:", user.username)
beginning(user)
