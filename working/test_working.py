from working import check_input

def test_valid_input():
    
    assert check_input("9 AM to 5 PM") == True
    assert check_input("9:00 AM to 5:00 PM") == True
    assert check_input("10 AM to 8:50 PM") == True
    assert check_input("11:15 AM to 6 PM") == True
    assert check_input("12:00 AM to 5:02 AM") == True
    assert check_input("12:01 AM to 5:34 AM") == True
    assert check_input("9 PM to 12:45 AM") == True
    
def test_invalid_input():
    
    assert check_input("9 AM - 5 PM") == False
    assert check_input("9:60 AM to 5:60 PM") == False
    assert check_input("09:00 AM - 17:00 PM") == False
    assert check_input("12 AM to 5:30 AM!") == False
    assert check_input("12:10 AM to ") == False
    assert check_input("12 AM to 6: AM") == False
    assert check_input("19:15 to 21:30") == False