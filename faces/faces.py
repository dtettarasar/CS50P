def main():

    str = convert_faces(input())

    print(str)


def convert_faces(str):

    # emoji unicodes
    smiling_face = "\U0001F642"
    frowning_face = "\U0001F641"

    str = str.replace(":)", smiling_face)
    str = str.replace(":(", frowning_face)

    return str

main()

