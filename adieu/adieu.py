def main():

    name_list = []

    while True:

        try: 
            name = input("Name: ")
            name_list.append(name)

        except EOFError:
            print()
            print("Adieu, goodbye, auf Wiederseh'n, Die Zeit mit dir war schön")
            print(name_list)
            break

main()