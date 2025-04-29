from um import count

def test_um():

    assert count('um') == 1

def test_long_sentence():

    assert count("um, hello, um, world") == 2

def test_case_insensitive():

    assert count("Um, thanks for the album.") == 1
