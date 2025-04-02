def main():

    str = input("What time it it? ")

    time = convert(str)

    # print(time)

    if 7 <= time <= 8:
        print("breakfast time")

    elif 12 <= time <= 13:
        print("lunch time")

    elif 18 <= time <= 19:
        print("dinner time")



def convert(time):

    time = time.split(":")
    # print(time)

    hours = float(time[0])
    minutes = float(time[1])
    minutes = minutes / 60

    # print(f"hours: {hours}")
    # print(f"minutes: {minutes}")

    converted_time = hours + minutes

    return converted_time


if __name__ == "__main__":
    main()
