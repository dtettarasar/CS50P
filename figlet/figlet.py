import sys
import random

from pyfiglet import Figlet

def main():

    font = get_font()

    print(font)

    # f = Figlet(font='alligator')
    # print(f.renderText('text to render'))


def get_font():

    # print(sys.argv)
    # print(len(sys.argv))

    font_list = [
        '3-d',
        '3x5',
    ]

    if len(sys.argv) == 1:

        print("random font")

        # Select a random item
        selected_font = random.choice(font_list)
        print(selected_font)

    elif len(sys.argv) == 3:

        print("chosen font")

    else:

        return False


main()
