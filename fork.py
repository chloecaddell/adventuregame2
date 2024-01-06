from player_info import *
from player_classes import *

def fork(user):
    character = user.character
    username = user.username
    stamina_check = user.stamina_check
    while (True):
        print(username, "The", character + ",",
              "You've arrived at a fork in the road. You can tell you are getting closer to the Fairy Village. Choose wisely.")
        fork_choice = input(
            "Would you like to follow the path to a 'COTTAGE', climb a 'TREE', or save a 'GIANT' tortoise? Choose COTTAGE OR TREE OR GIANT: ")
        fork_choice = fork_choice.lower()
        print("\n")
        if fork_choice == "cottage":
            print(username + "," + "You've arrived at the cottage. Inside you meet some humans gathered around cooking a feast. They challenge you to a cook off!")
            if character == frog_wizard or character == corgi_cleric:
                print(
                    "--Congratulations!", username, "The", character, "You've won the cook off! The humans decide to give you directions to the Fairy Village!--")
                stamina_check()
                exit()
            elif character == cat_rogue or character == cow_barbarian:
                user.stamina = user.stamina - 2
                print(
                    "You lost the cook off:( The humans tried to eat you. Lose 2 stamina and return to the fork in the road.")
                stamina_check()
                continue
        elif fork_choice == "tree":
            print(
                "You decide to climb the tree to try and see a way to the Fairy Village.")
            if character == frog_wizard or character == cat_rogue:
                print(
                    "--Congratulations!", username, "The", character, "You see the way to the Fairy Village and climb down the tree safely. You then start your trek to the village.--")
                stamina_check()
                exit()
            elif character == cow_barbarian or character == corgi_cleric:
                user.stamina = user.stamina - 2
                print(character + "'s" +
                      " cannot climb trees. You fell and lost 2 stamina. Return to the fork in the road.")
                stamina_check()
                continue
        elif fork_choice == "giant" or fork_choice == "giant tortoise":
            print("The giant tortoise is trapped under a fallen tree.")
            if character == cow_barbarian or character == frog_wizard:
                if character == cow_barbarian:
                    print("--Congratulations!", username, "The", character, "with your strength you lift the tree off the tortoise. The tortoise is so thankful they let you ride them to the Fairy Village.--")
                    stamina_check()
                    exit()
                elif character == frog_wizard:
                    print("--Congratulations!", username, "The", character, "with your magic you turn the tree into soft flower petals, freeing the giant tortoise. The giant tortoise is forever in your debt and guides you to the Fairy Village.--")
                    stamina_check()
                    exit()
            elif character == cat_rogue or character == corgi_cleric:
                user.stamina -= 2
                print(
                    "You are unable to save the giant tortoise. Lose 2 stamina and return to the fork in the road.")
                stamina_check()
                continue
        else:
            continue