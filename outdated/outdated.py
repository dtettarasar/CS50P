def main():

    date_dict = None

    while True:

        date = input("Date: ")
        date_dict = get_dict(date)

        if date_dict != False:
            break

    final_format = convert_to_final_format(date_dict)
    print(final_format)


# build another function that will take the date dict as parameter and convert it to the final request format (YYYY-MM-DD) and then return it, so that it can be printed in the main function

def get_dict(date):

    date_dict = None

    # identify if the input is following one of the two valid format (short or long)

    # to identify if short:
    # - it should be composed by 3 integer separated by 2 slashes

    # to identify is long:
    # month, day and year should be separated by a single space

    # print(date)

    date = date.strip()

    slashes = date.count('/')
    spaces = date.count(' ')

    # print(f"slashes: {slashes}")
    # print(f"spaces: {spaces}")

    # if dates elements are separated by 2 slashes, then it is following the short format
    # else if dates elements are separated by 2 spaces, then it is following the long format

    if slashes == 2 and spaces == 0:

        # print("short format date")

        date_list = date.split('/')
        date_dict = convert_from_short(date_list)

    elif spaces == 2 and slashes == 0:

        # print("long format date")

        date_list = date.split(' ')
        date_dict = convert_from_long(date_list)

    else:

        # print ("the string does not correspond to any valid date format")
        return False

    # Below are the conditions that need to be checked for both date formats
    # - the month should be superior or equal to 1 and inferior or equal to 12
    # - the day should be superior or equal to 1 and inferior or equal to 31

    # check first that we have a valid date dictionary
    if date_dict != False:

        if date_dict["month"] < 1 or date_dict["month"] > 12:
            # print("month is not valid: it should not equal to 0 or superior to 12")
            return False

        if date_dict["day"] < 1 or date_dict["day"] > 31:
            # print("day is not valid: it should not equal to 0 or superior to 31")
            return False

    # print(date_dict)

    return date_dict


def convert_from_short(date_list):

    date_dict = {

        "day": 0,
        "month": 0,
        "year":0

    }

    # print(date_list)

    # make sure we only have digits in the list
    for elem in date_list:

        if elem.isdigit() != True:
            # print ("not valid format: one or more element are not digits")
            return False

    # then convert it to a dict containing 3 key-values pairs : day, month, year. All 3 values should store the date element values as int format

    date_dict["day"] = int(date_list[1])
    date_dict["month"] = int(date_list[0])
    date_dict["year"] = int(date_list[2])

    return date_dict


def convert_from_long(date_list):

    date_dict = {

        "day": 0,
        "month": 0,
        "year":0

    }

    month_values = {

        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12

    }

    # print(date_list)

    # check that the first element in the date list correspond to a fullwritten month
    # written in full format ("January","February", [...], "December")

    month = month_values.get(date_list[0])

    if month == None:

        # print ("not valid format: the first element is not a valid month")
        return False

    else:

        # we have a valid month format, we can store it in the dict
        date_dict["month"] = month


    # check that the second element is a day formatted in the proper way (digit followed by one comma)

    day = date_list[1]

    if day.endswith(",") == False or day.count(",") != 1:

        # print("not valid format: the day element does not end with a single comma")
        return False

    day = day[:-1]
    # print(day)

    if day.isdigit() != True:

        # print ("not valid format: the day element is not a digit")
        return False

    else:

        # we have a valid day format we can store it in the dict
        date_dict["day"] = int(day)


    # check that the last element is a year formatted in the proper way (digit)

    year = date_list[2]

    if year.isdigit() != True:

        # print ("not valid format: the year element is not a digit")
        return False

    else:

        # we have a valid year format we can store it in the dict
        date_dict["year"] = int(year)

    # then convert it to a dict containing 3 key-values pairs : day, month, year. All 3 values should store the date element values as int format

    return date_dict


def convert_to_final_format(date_dict):

    # print(date_dict)

    # day = date_dict["day"] < 10 ? f"0{date_dict["day"]}" : f"{date_dict["day"]}"
    # month = date_dict["month"] < 10 ? f"0{date_dict["month"]}" : f"{date_dict["month"]}"

    day = f"0{date_dict["day"]}" if date_dict["day"] < 10 else f"{date_dict["day"]}"
    month = f"0{date_dict["month"]}" if date_dict["month"] < 10 else f"{date_dict["month"]}"
    year = date_dict["year"]

    # print("final format")
    # print(f"{year}-{month}-{day}")

    final_format = f"{year}-{month}-{day}"

    return final_format


main()
