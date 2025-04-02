def main():

    item_list = []

    while True:

        try:

            item = input()

            item_list = update_item_list(item_list, item)

            # print("item list after update")


        except EOFError:
            print()
            display_item_list(item_list)
            break


def update_item_list(item_list_param, item_param):

    # print("init update item list")

    # print('item_list: ')

    # print(item_list_param)

    # print('item')

    # print(item_param)

    # check if an item is already in the list, if the item is found then update the quantity

    for item in item_list_param:

        # print("init for loop")

        if item['name'] == item_param.lower():

            item['quantity'] += 1
            return item_list_param


    # if the item parameter is not yet in the list, then create its dict and add it to the list

    new_item = {

        "name": item_param,
        "quantity": 1

    }

    item_list_param.append(new_item)

    # print("list updated:")
    # print(item_list_param)

    return item_list_param


def display_item_list(item_list_param):

    # print(item_list_param)

    sorted_list = sorted(item_list_param, key=lambda x: x['name'])

    # print(sorted_list)

    for item in sorted_list:

        # print(item)

        print(f"{item['quantity']} {item['name'].upper()}")

main()

