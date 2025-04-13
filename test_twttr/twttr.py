def main():

    str = input("Input: ")

    str_without_vowels = remove_vowels(str)

    print(f"Output: {str_without_vowels}")

def remove_vowels(str):

    vowels_list = [
        "A", "E", "I", "O","U",
        "a","e","i","o","u"
    ]

    char_list = []

    for s in str:

        # print(s)

        if s not in vowels_list:

            char_list.append(s)

    # print(char_list)

    result = ''.join(char_list)

    return result


if __name__ == "__main__":
    main()
