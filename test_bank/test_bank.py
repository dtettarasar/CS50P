from bank import value

def test_invalid_input():
    assert value("Test") == None

def test_zero_dollar():

    assert value("Hello") == "$0"
    assert value("Hello, Newman") == "$0"



if __name__ == "__main__":
    main()