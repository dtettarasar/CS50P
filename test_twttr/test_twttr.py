from twttr import shorten


def test_lowercase():

    assert shorten("metallica") == "mtllc"

def test_uppercase():

    assert shorten("KORN") == "KRN"

def test_punctuations():

    assert shorten("What's your name?") == "Wht's yr nm?"

def test_numbers():

    assert shorten("This Was CS50") == "Ths Ws CS50"

if __name__ == "__main__":
    main()

