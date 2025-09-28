"""
Program Name: Lab5_ssrinivasan3-#02.py

Author: Shrrayash Srinivasan

Purpose: I am to create a game called “Pick Up Sticks”. I must translate the puesdocode from the lab sheet 
to a python language

Date: September 23, 2025
"""
# Set maximum amount of sticks a person can take to 4.

MAX_Sticks = 4
MIN_Sticks = 1
TOTAL_Sticks = 13

current_player = 1

# Print out the instructions for the game.

print ("Hello! Welcome to the game, Pick Up Sticks!")

print ("Each player takes turns picking up from", MIN_Sticks, "sticks to", MAX_Sticks, "sticks." )

print ("Last player to get the final stick wins the game!" )

print ("There are", TOTAL_Sticks, "sticks left")

# While there are more than 0 sticks left, keep the game going

while TOTAL_Sticks > 0:
    print ("Player", current_player, "it is your turn.")
    picked_sticks = int(input("How much sticks you wish to pick up?"))

    if picked_sticks < MIN_Sticks or MAX_Sticks < picked_sticks: 
        print ("Sorry! But you can only pick up between", MIN_Sticks, "and", MAX_Sticks, "sricks. Try agaiin")
        continue
    
    #    Reduce number of sticks in pile by number of sticks current player asked to take

    TOTAL_Sticks = TOTAL_Sticks - picked_sticks
    print ("You got", TOTAL_Sticks,"sticks left!" )

    #Create condition once you win the game
    if TOTAL_Sticks == 0:
        print ("Congratualations!" "Player", current_player, "wins the game!")
        break

    
    # Trade players per turn
    if current_player == 1:
       current_player = 2
    else:
        current_player = 1
    

