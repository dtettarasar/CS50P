def main():

    str = input("Greeting: ").strip()

    answer = value(str)

    if answer != None:
        print(answer)


def value(greeting):

    if (greeting == "Hello" or greeting == "Hello, Newman"):
        #  print("$0")
        return 0

    elif (greeting == "How you doing?"):
        # print("$20")
        return 20

    elif (greeting == "What's happening?" or greeting == "What's up?"):
        # print("$100")
        return 100

    else:

        return None


if __name__ == "__main__":
    main()
