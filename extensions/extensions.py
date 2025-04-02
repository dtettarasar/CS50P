
def main():

    str = input("File name: ").strip().lower()
    # print(str)

    file_format = get_format(str)

    # print(file_format)

    if file_format:
        print(get_mime_type(file_format))

    else:
        print("application/octet-stream")



# check that str contain one dot. if yes then return what's after the dot to get the file format
def get_format(str):

    # str.count(".") == 1:

    if str.count(".") == 1:
        # print("String format is valid")
        format = str.split(".")
        return format[1]

    elif str.count(".") == 2:
        # print("String format is valid")
        format = str.split(".")
        return format[2]

    else:
        # print("String format is not valid")
        return False


# get the mime type based on the file extension
def get_mime_type(file_format):

    # print("start get_mime_type method")

    mime_types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip"
    }

    # print(file_format)

    # if 'key1' in dict.keys():

    if file_format in mime_types.keys():

        # print('mime type object has attribute')
        return mime_types[file_format]

    else:

        return "application/octet-stream"

main()
