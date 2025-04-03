# https://cs50.harvard.edu/python/2022/psets/4/game/

import random

def main():

    level = ""

    while level.isdigit() == False:

        level = input("Level: ")
    
    print(f"level selected is: {level}")

    number_to_guess = random.randint(1, int(level))

    print(f"number to guess: {number_to_guess}") 

main()