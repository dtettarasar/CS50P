def main():

    while True:

        try: 
            name = input("Name: ")

        except EOFError:
            print()
            print("Adieu, goodbye, auf Wiederseh'n")
            break

main()