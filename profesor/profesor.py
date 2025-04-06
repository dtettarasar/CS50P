import random


def main():
    # todo

    str = input("Level: ")

    print(get_level(str))


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
