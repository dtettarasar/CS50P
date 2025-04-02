def main():

    amount_due = 50

    while amount_due > 0:

        coin = ask_for_coin()
        # print(coin)

        # if a valid coin is given by the user, then substract the coin value to the amount due, until it reaches 0
        if coin != False:
            amount_due = amount_due - coin

        if amount_due > 0:
            print(f"Amount Due: {amount_due}")


    change_owed = amount_due * -1

    print(f"Change Owed: {change_owed}")



# make sure the user provide a value corresponding to a valid coin
def ask_for_coin():

    valid_coins = [
        25,
        10,
        5
    ]

    coin = input("Insert coin: ")

    if coin.isdigit():

        coin = int(coin)

        if coin in valid_coins:

            return coin

        else:

            return False

    else:

        return False


main()
