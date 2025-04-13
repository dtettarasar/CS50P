from twttr import remove_vowels


def test_lowercase():

    assert remove_vowels("metallica") == "mtllc"

def test_uppercase():

    assert remove_vowels("KORN") == "KRN"

    
if __name__ == "__main__":
    main()

