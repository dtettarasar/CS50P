from twttr import shorten


def test_lowercase():

    assert shorten("metallica") == "mtllc"

def test_uppercase():

    assert shorten("KORN") == "KRN"

    
if __name__ == "__main__":
    main()

