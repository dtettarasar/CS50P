import emoji

def main():

    str = input("Input: ")

    emojized_str = emoji.emojize(str, language='alias')

    print(f'Output: {emojized_str}')


main()
