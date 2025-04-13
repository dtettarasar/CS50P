from plates import is_valid

def test_valid_plate():

    assert is_valid("CS50") == True

def test_no_alphabectical_start():

    assert is_valid("12") == False

def test_wrong_length():

    assert is_valid("H") == False

def test_wrong_num_placement():

    assert is_valid("AAA22A") == False

def test_zero_placement():

    assert is_valid("CS05") == False

def test_non_alphanumeric_chars():

    assert is_valid("PI3.14") == False
