from bank import value

def test_zero_dollar():

    assert value("Hello") == 0
    assert value("Hello, Newman") == 0

def test_twenty_dollars():

    assert value("How you doing?") == 20

def test_hundred_dollars():

    assert value("What's happening?") == 100
    assert value("What's up?") == 100
