# https://cs50.harvard.edu/python/2022/psets/4/game/

import random
import sys

def main():

    level = ""

    while check_level(level) == False:

        level = input("Level: ")

        check_level(level)


    # print(f"level selected is: {level}")

    number_to_guess = random.randint(1, int(level))

    # print(f"number to guess: {number_to_guess}")

    result = False
    user_guess = ""

    while user_guess.isdigit() == False or result == False:

        user_guess = input("Guess: ")

        if user_guess.isdigit() == True:

            result = get_result(number_to_guess, int(user_guess))

            if result == True:
                sys.exit("Just Right!")

# Make sure the level provided by the user correspond to a positiv integer
def check_level(level):

    # print('init check level func')
    # print("is level a digit")

    if level.isdigit() == False:

        return False
    
    else:

        int_level = int(level)

        if int_level > 0:

            return True
        
        else: 

            return False


def get_result(number_to_guess, user_guess):

    if user_guess < number_to_guess:
        print("Too small!")
        return False

    elif user_guess > number_to_guess:
        print("Too large!")
        return False

    else:
        # print('Just right!')
        return True


main()
