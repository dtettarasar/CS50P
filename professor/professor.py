import random

def main():

    level = get_level()

    int_list = generate_integer(int(level))

    math_pb_list = generate_math_pb_list(int_list)

    play_game(math_pb_list)


def get_level():

    level = False

    levels_list = ["1", "2", "3"]

    while level == False:

        level = input("Level: ")

        if level not in levels_list:

            level = False

        else:

            break

    return level

def generate_integer(level):

    # print("generate integer function")
    # print(level)

    int_list = []

    range_start_number = 0
    range_end_number = 0

    # print('init generate_int function')
    # print(f"Level: {level}")

    if level == 1:

        range_end_number = 9

    elif level == 2:

        range_start_number = 10
        range_end_number = 99

    elif level == 3:

        range_start_number = 100
        range_end_number = 999

    # print(f"int generated: {int}")

    # return int

    for _ in range(20):

        int = random.randint(range_start_number, range_end_number)

        int_list.append(int)

    # print(int_list)

    return int_list


def generate_math_pb_list(int_list):

    # print('init math_pb_list function')
    # print('int list')
    # print(int_list)

    math_pb_list = []

    for i in range(len(int_list)):

        # print(int_list[i])

        if (i % 2) == 0:
              
            # checker si i est pair
            # si i est pair alors int_one = int_list[i] et int_two = int_list[i + 1]

            # print (f"{int_list[i]} + {int_list[i+1]}")

            math_pb_dict = {

                "int_one": int_list[i],
                "int_two": int_list[i+1],
                "solved": False, # track is the user solved the math problem
                "remaining_attempts": 3 # to track the number of tries made by the user. each time the user failed to solve the problem, decrease the value by 1. and if it reaches 0 go to next problem

            }

            math_pb_dict["result"] = math_pb_dict["int_one"] + math_pb_dict["int_two"]

            # print(math_pb_dict)

            math_pb_list.append(math_pb_dict)

    return math_pb_list


def play_game(math_pb_list):

    # print('init the the play game function')

    # print(math_pb_list)

    player_score = 0

    for math_pb_dict in math_pb_list:

        # print(math_pb_dict)

        while math_pb_dict["remaining_attempts"] != 0 and math_pb_dict["solved"] == False:

            answer = input(f"{math_pb_dict["int_one"]} + {math_pb_dict["int_two"]} = ")

            if answer.isdigit() == True:

                answer_int = int(answer)

                if answer_int == math_pb_dict["result"]:

                    # print('right answer found')
                    math_pb_dict["solved"] = True
                    player_score += 1

                else:

                    math_pb_dict["remaining_attempts"] -= 1

                    print("EEE")
                    # print("remaining_attempts: ")
                    # print(math_pb_dict["remaining_attempts"])

            else:

                math_pb_dict["remaining_attempts"] -= 1

                print("EEE")
                # print("remaining_attempts: ")
                # print(math_pb_dict["remaining_attempts"])


    # print(math_pb_list)
    print(f"Score: {player_score}")




if __name__ == "__main__":
    main()
