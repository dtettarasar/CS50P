import sys

def main():

    get_arg()

def get_arg():

    arg = sys.argv

    print(arg)

    if len(arg) == 1:

        sys.exit('Missing command-line argument')

main()