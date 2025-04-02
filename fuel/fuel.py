def main():

    fraction = False

    # ask the user for an input until a valid fraction is provided
    while fraction == False:

        fraction = get_fraction()

        # make the division : if the divisor is equal to zero, make_division will return False, thus the program remain in the loop, to ask again for another fraction
        if fraction != False:

            fraction = make_division(fraction)

    print(fraction)


def make_division(fraction):

    # print('init make division function')

    # print(fraction)

    result = None

    # Make sure the dividend is inferior to the divisor

    try:

        if fraction["dividend"] > fraction["divisor"]:

            # print('error: dividend cannot be superior to divisor')

            return False

        result = fraction["dividend"] * 100 / fraction["divisor"]

        if result <= 1:

            return "E"

        elif result >= 99:

            return "F"

        else:

            return f"{round(result)}%"

    except ZeroDivisionError:

        # print("cannot divide by zero")

        return False


def get_fraction():

    fraction = {
        "dividend": None,
        "divisor": None
    }

    str = input('Fraction: ')

    # To make sure the string match the fraction format
    slash_check = str.count('/')

    str_list = None

    # print(str)
    # print(f"slash: {slash_check}")

    if slash_check == 1:

        str_list = str.split('/')

    else:

        return False

    fraction["dividend"] = str_list[0]
    fraction["divisor"] = str_list[1]

    # print(f"dividend: {dividend}")
    # print(f"divisor: {divisor}")

    # try to convert the list parameters to int
    try:

        fraction["dividend"] = int(fraction["dividend"])
        fraction["divisor"] = int(fraction["divisor"])

    except ValueError:

        # print("values not valid")

        return False

    else:

        return fraction


main()
