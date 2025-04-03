# https://cs50.harvard.edu/python/2022/psets/4/game/

import random

def main():

    level = ""

    while level.isdigit() == False:

        level = input("Level: ")
    
    print(f"level selected is: {level}")

    number_to_guess = random.randint(1, int(level))

    print(f"number to guess: {number_to_guess}")

    result = False
    user_guess = ""

    while user_guess.isdigit() == False or result == False:

        user_guess = input("Guess: ")

        if user_guess.isdigit() == True:

            result = get_result(number_to_guess, int(user_guess))



def get_result(number_to_guess, user_guess):

    if user_guess < number_to_guess:
        print("Too small!")
        return False
    
    elif user_guess > number_to_guess:
        print("Too large!")
        return False
    
    else:
        print('Just right!')
        return True 


main()