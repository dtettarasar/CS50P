import random


def main():
    # todo

    level = ""

    while get_level(level) == False:

        level = input("Level: ")

        # level = get_level(str)

    print(level)


def get_level(str):
    # todo

    print("init get level function")

    levels_list = ["1", "2", "3"]

    if str not in levels_list:

        return False
    
    else:

        return True


def generate_integer(level):
    # todo

    print('generate integer function')


if __name__ == "__main__":
    main()
