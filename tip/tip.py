def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):

    formatted_value = d.replace("$", "")
    formatted_value = float(formatted_value)

    # print( formatted_value)

    return formatted_value


def percent_to_float(p):

     formatted_value = p.replace("%", "")
     formatted_value = float(formatted_value)/100

     return formatted_value

main()

