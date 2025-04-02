import sys
import random

from pyfiglet import Figlet

def main():

    selected_font = get_font()

    print(selected_font)

    if selected_font == False:

        sys.exit('Invalid usage')

    else:

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
        
        selected_font = random.choice(font_list)

        return selected_font

    elif len(sys.argv) == 3:

        print("chosen font")

        if sys.argv[2] in font_list:

            return sys.argv[2]
        
        else:

            return False

    else:

        return False


main()
