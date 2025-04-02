import sys
import random

from pyfiglet import Figlet

def main():

    selected_font = get_font()

    print(selected_font)

    f = Figlet(font=selected_font)
    print(f.renderText('text to render'))


def get_font():

    # print(sys.argv)
    # print(len(sys.argv))

    # font_list_bis = Figlet().getFonts()

    # print(font_list_bis)

    font_list = Figlet().getFonts()

    if len(sys.argv) == 1:

        print("random font")

        # Select a random item
        selected_font = random.choice(font_list)
        # print(selected_font)

        return selected_font

    elif len(sys.argv) == 3:

        print("chosen font")

        if sys.argv[2] in font_list:

            return sys.argv[2]

    else:

        return False


main()
