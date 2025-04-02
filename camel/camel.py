def main():

    variable = input('camelCase: ')

    # split the str into an array
    variable_char_list = list(variable)

    uppercase_letter_index = find_uppercase(variable_char_list)

    add_underscores(variable_char_list, uppercase_letter_index)

    variable_char_list = change_to_lowercase(variable_char_list)

    result = ''.join(variable_char_list)

    print(f"snake_case: {result}")


def find_uppercase(char_list):

    # print(char_list)

    uppercase_letter_index = []

    # loop in the array and check if the char is an uppercase letter
    for i in range(len(char_list)):

        char = char_list[i]

        is_char_upper = char.isupper()

        # print(f"{i}: {char}: {is_char_upper}")

        # if True: keep track of the index of the found uppercase letters
        if is_char_upper == True:

            # print("found uppercase letter")

            uppercase_letter_index.append(i)

            # char_list.insert(i, "_")

    # print(char_list)
    # print(uppercase_letter_index)

    # add_underscores(char_list, uppercase_letter_index)

    return uppercase_letter_index


def add_underscores(char_list, uppercase_letter_index):

    for i in range(len(uppercase_letter_index)):

        letter_index = uppercase_letter_index[i]

        # Add an underscore before the uppercase letter in the array
        # Make sure to add i to the letter index: as each time we add an uppercase in the list before an uppercase letter, the index of the next uppercase letter changes
        char_list.insert(letter_index + i, "_")
        # print(char_list[letter_index]);

    # print(char_list)


def change_to_lowercase(char_list):

    new_char_list = []

    for i in range(len(char_list)):

        char = char_list[i]

        is_char_upper = char.isupper()

        if is_char_upper == True:

            new_char_list.append(char.lower())

        else:

            new_char_list.append(char)


    # print(char_list)
    # print(new_char_list)

    return new_char_list


main()
