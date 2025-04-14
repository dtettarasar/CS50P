def main():
    
    fraction = False

    while fraction in [False, None]:

        str = input('Fraction: ')

        fraction = convert(str)

    print(fraction)


def convert(str):

    fraction = {
        "dividend": None,
        "divisor": None
    }

    result = None

    # To make sure the string match the fraction format
    slash_check = str.count('/')

    str_list = None

    if slash_check == 1:

        str_list = str.split('/')

    else:

        return False

    fraction["dividend"] = str_list[0]
    fraction["divisor"] = str_list[1]

    # try to convert the list parameters to int
    try:

        fraction["dividend"] = int(fraction["dividend"])
        fraction["divisor"] = int(fraction["divisor"])

    except ValueError:

        # print("values not valid")

        return False

    try:

        if fraction["dividend"] > fraction["divisor"]:

            # print('error: dividend cannot be superior to divisor')

            return False
        
        else:

            result = fraction["dividend"] * 100 / fraction["divisor"]

            return round(result)

    except ZeroDivisionError:

        return False 


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
