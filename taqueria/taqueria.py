def main():

    total_price = 0.00

    while True:

        try:

            item = input("Item: ")
            price = get_price(item)
            # print(get_price(item))

            if price != False:

                total_price += price

                print(f'Total: ${round(float(total_price),2):.2f}')

        except EOFError:
            print()
            break


def get_price(item_param):

    # print("init get price function")

    # print(item_param)

    item_list = [

        {
            "name": "baja taco",
            "price": 4.25
        },

        {
            "name": "burrito",
            "price": 7.50
        },

        {
           "name":"bowl",
           "price": 8.50
        },

        {
            "name": "nachos",
            "price": 11.00
        },

        {
            "name": "quesadilla",
            "price": 8.50
        },

        {
            "name": "super burrito",
            "price": 8.50
        },

        {
            "name": "super quesadilla",
            "price": 9.50
        },

        {
            "name": "taco",
            "price": 3.00
        },

        {
            "name": "tortilla salad",
            "price": 8.00
        },

    ]

    for item in item_list:

        if item['name'] == item_param.lower():

            # print(item)

            # print(round(item['price'], 2))

            return round(item['price'], 2)

    return False



main()
