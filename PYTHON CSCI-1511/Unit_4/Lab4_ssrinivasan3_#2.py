"""
Program Name: Lab4_ssrinivasan3_#2.py

Author: Shrrayash Srinivasan

Purpose: Write a program that asks the player to guess a random number between 1 and 15. If the guess is incorrect, 
the next body part is added to the hangman. If correct, print out a congratulatory greeting. The game over is the number of 
wrong guesses is the length of the list of triple quoted strings. 

Date: September 16, 2025
"""
import random

#Enter a random number between 1 and 15

number = random.randint(1,15)

hangman_list = [
    """ 
    ------|
    |
    |
    |
    |
    """,
    """
    ------|
    |     o
    |
    |
    |
    """,
    """
    ------|
    |     o
    |     |
    |
    |
    """ ,
    """
    ------|
    |     o
    |    /|
    |
    |
    """,
       """
    ------|
    |     o
    |    /|\\
    |
    |
    """,
    """
    ------|
    |     o
    |    /|\\
    |    /
    |
    """,
        """
    ------|
    |     o
    |    /|\\
    |    / \\
    |
    """

    ]

print ("Let's get this game started! All you gotta do is gueess a number between 1 and 15, if you get it a wrong, a part of the hangman will be added! If you win, you win, and you will nto recieve a mocking message!")

if __name__== "__main__":
    guess = int(input("Number that is between 1 and 15. Insert here: "))
    wrong_guesses = 7
    while wrong_guesses > 0:
        if guess == number:
            print ("Nice job, dude! You rock and bested this round. The number was", number,".")
            break
        else:
            print(hangman_list[7 - wrong_guesses])
            wrong_guesses -= 1
            if wrong_guesses == 0:
                print ("You suck!! The correct number is", number, "you lousy guesser!")
                break
            else:
                guess = int(input("Wrong! Try again! You got " + str(wrong_guesses) + " more guesses left! Number: "))


        
            






    



   




    
