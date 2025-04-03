# https://cs50.harvard.edu/python/2022/psets/4/adieu/
import inflect

def main():

    p = inflect.engine()

    name_list = []

    while True:

        try: 
            name = input("Name: ")
            name_list.append(name)

        except EOFError:

            print()
            # print("Adieu, goodbye, auf Wiederseh'n, Die Zeit mit dir war schön")
            # print(name_list)

            lastStr = p.join(name_list , ",")
            print(f'Adieu, adieu, to {lastStr}')

            break

main()