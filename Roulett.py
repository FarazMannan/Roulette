# random number gen.

import random

# intro to the game

print("")

# adding and subrtacting system

# bank

bank = 500

# asking the player to enter one of 3 color choices (input)

keep_gambling = True
while keep_gambling == True:
    color_selected = input("What color would you like to pick? ")
    color_selected = color_selected.lower()

    # the different color choices in a compiled list

    color = [
        "green",
        "red",
        "black",
    ]

    # random number generator

    random_number = random.randint(0,2)
    color_the_ball_lands_on = color[random_number]

    # printing the random number generator, what the program says the correct
    # color is
    if color_selected == color_the_ball_lands_on:
        winner_winner_chicken_dinner = True
    else:
        winner_winner_chicken_dinner = False

    if winner_winner_chicken_dinner == True:
        print("You win!")
    else:
        print("You lost!")

        # need to add a bank
        # subtracting and adding the balance off of wins
        # and loses

    if winner_winner_chicken_dinner == True:
        bank = bank + 50
    else:
        bank = bank - 50

    dollars_in_pocket = str(bank)
    print("Dollars in Pocket: $" + dollars_in_pocket)

    if bank <= 0:
        keep_gambling = False
        print("You have lost all of your money. Goodbye")
    elif bank >= 1000:
        keep_gambling = False
        print("Know when to hold em, know when to fold em, know when to walk away...")
        print("Congrats on walking away with $1,000!")
