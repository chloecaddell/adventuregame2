from player_info import *
from player_classes import *
from meadow import *

def pond_cave(user):
    character = user.character
    username = user.username
    stamina_check = user.stamina_check
    while (True):
        if character == corgi_cleric or character == cat_rogue:
            print("You've stumbled across a pond.")
            break
        elif character == frog_wizard or character == cow_barbarian:
            user.stamina -= 2
            print("Looks like you've gotten lost in a cave. Lose 2 stamina.")
            stamina_check()
            break
    pond = input(username + "," +
                 " You've arrived at a pond. Would you like to swim or go around the pond? Choose 'SWIM' OR 'GO AROUND': ")
    pond = pond.lower()
    print("\n")
    while (True):
        if pond == "swim":
            if character == frog_wizard or character == corgi_cleric:
                user.stamina -= 3
                print("Swimming has taken a lot out of you, lose 3 stamina.")
                stamina_check()
                meadow(user)
                break
            elif character == cat_rogue or character == cow_barbarian:
                user.stamina -= 1
                print("Swimming is quick, only lose 1 stamina.")
                stamina_check()
                meadow(user)
                break
        elif pond == "go around":
            user.stamina -= 2
            print("Walking is a lot of work, lose 2 stamina.")
            stamina_check()
            meadow(user)
            break
        else:
            print("Looks like you've entered something wrong. Try again.")
            continue