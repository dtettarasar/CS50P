# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import sys
import requests

def main():

    qty = get_arg()

    get_price_index(qty)


def get_arg():

    arg = sys.argv

    # print(arg)

    if len(arg) == 1:

        sys.exit('Missing command-line argument')

    elif len(arg) != 2:

        sys.exit("You should provide only one command-line argument")

    else:

        try:

            return float(arg[1])

        except ValueError:

            sys.exit("Command-line argument is not a number")


def get_price_index(qty):

    # print("init get price index")

    # print(qty)

    r = None

    price = 0

    try:

        r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=ca296c840c2b68d060a5e503474ec1540aa8535ca5cd9112b575567f61523155')

    except requests.RequestException:

        sys.exit("Error with the API Call")

    r_json = r.json()

    try:

        price = r_json['data']['priceUsd']

    except KeyError:

        sys.exit("Price is not available")

    # print(price)

    price_float = float(price)

    index = price_float * qty

    # print(index)

    print(f"${index:,.4f}")


main()