# https://cs50.harvard.edu/python/2022/psets/4/figlet/
import sys
import random

from pyfiglet import Figlet

def main():

    selected_font = get_font()

    # print(selected_font)

    if selected_font == False:

        sys.exit('Invalid usage')

    else:

        str = input("Input: ")

        f = Figlet(font=selected_font)

        print("Output: ")
        print(f.renderText(str))


def get_font():

    font_list = Figlet().getFonts()

    if len(sys.argv) == 1:

        # print("random font")

        selected_font = random.choice(font_list)

        return selected_font

    elif len(sys.argv) == 3:

        # print("chosen font")

        first_argument = ['-f', '--font']

        if sys.argv[1] not in first_argument:

            return False

        if sys.argv[2] in font_list:

            return sys.argv[2]
        
        else:

            return False

    else:

        return False


main()
