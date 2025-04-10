import sys

def main():

    qty = get_arg()

    print(qty)

def get_arg():

    arg = sys.argv

    # print(arg)

    if len(arg) == 1:

        sys.exit('Missing command-line argument')

    elif len(arg) != 2:

        sys.exit("You should provide only one command-line argument")

    else:

        try:

            return float(arg[1])

        except ValueError:

            sys.exit("Command-line argument is not a number")

main()