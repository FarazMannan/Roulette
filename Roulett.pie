import random 

#intro to the game

print("")

#asking the player to enter one of 3 color choices (input)

color_selected = input("What color would you like to pick? ")
color_selected = color_selected.lower()

#the different color choices in a compiled list

color = [
    "green",
    "red",
    "black",
]

#random number generator

random_number = random.randint(0,2)
color_the_ball_lands_on = color[random_number]

#printing the random number generator, what the program says the correct
#color is
if color_selected == color_the_ball_lands_on:
    winner_winner_chicken_dinner = True
else:
    winner_winner_chicken_dinner = False

if winner_winner_chicken_dinner == True:
    print("You win!")
else:
    print("You lost")
