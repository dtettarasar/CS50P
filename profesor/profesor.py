import random


def main():
    # todo

    level = ""

    while get_level(level) == False:

        level = input("Level: ")

        # level = get_level(str)

    generate_math_pb_list(level)


def get_level(str):
    # todo

    print("init get level function")

    levels_list = ["1", "2", "3"]

    if str not in levels_list:

        return False
    
    else:

        return True


def generate_int(level):
    # todo

    range_start_number = 0
    range_end_number = 0


    # print('init generate_int function')
    # print(f"Level: {level}")

    if level == "1":

        range_end_number = 9
    
    elif level == "2":

        range_start_number = 10
        range_end_number = 99

    elif level == "3":

        range_start_number = 100
        range_end_number = 999

    int = random.randint(range_start_number, range_end_number)

    # print(f"int generated: {int}")

    return int


def generate_math_pb_list(level):

    print('init math_pb_list function')

    math_pb_list = []

    generate_int(level)

    for i in range(10):

        math_pb_dict = {

            "int_one": generate_int(level),
            "int_two": generate_int(level),

        }

        print(f"{math_pb_dict["int_one"]} + {math_pb_dict['int_two']}")


def play_game(mth_pb_list):
    
    print('init the the play game function')



if __name__ == "__main__":
    main()
