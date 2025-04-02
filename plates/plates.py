def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):
    # print(string)

    # char_list = s.split('')

    # check that the plate as a valid length
    if len(string) < 2 or len(string) > 6:
        return False

    for i in range(len(string)):

        char = string[i]

        # check that the first two characters are letters
        if i == 0 or i == 1:
            if string[i].isalpha() == False:
                return False

        # check that the remaining characters in the string are letters or numbers
        elif string[i].isalnum() == False:
            return False

        # print(char)

    if start_with_zero(string) == False or has_full_number_seq(string) == False:
        return False

    return True

# check if the number sequence start with zero
def start_with_zero(string):

    # print("init start_with_zero function")

    first_int = None

    for char in string:
        # print(char)

        if char.isdigit():
            # print(f'first int found!: {char}')
            first_int = char
            break

    if first_int == "0":
        return False

    else:
        return True

# check that once a number sequence is found in the plates, it is not cut by a non digit char
def has_full_number_seq(string):

    # print("init has_full_number_seq function")

    first_int_found = None

    for char in string:

        if char.isdigit() and first_int_found == None:

            first_int_found = True

        elif first_int_found == True and char.isdigit() == False:

            return False

    return True

main()
