def main():

    str = input("Greeting: ").strip()

    answer = value(str)

    if answer != None:
        print(f"${answer}")


def value(greeting):

    greeting_lc = greeting.lower()

    if (greeting_lc.startswith("hello")):
        #  print("$0")
        return 0

    elif (greeting_lc.startswith("h")):
        # print("$20")
        return 20

    else:

        return 100


if __name__ == "__main__":
    main()
