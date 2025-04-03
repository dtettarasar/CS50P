# https://cs50.harvard.edu/python/2022/psets/4/game/

def main():

    level = ""

    while level.isdigit() == False:

        level = input("Level: ")
    
    print(f"level selected is: {level}")

main()