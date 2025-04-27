from working import check_input, format_to_twenty_four

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
    
def test_format_time():
    
    assert format_to_twenty_four("12:45 AM") == "00:45"
    assert format_to_twenty_four("12:45 PM") == "12:45"
    assert format_to_twenty_four("12:01 AM") == "00:01"
    assert format_to_twenty_four("9 AM") == "09:00"
    assert format_to_twenty_four("5:00 PM") == "17:00"
    assert format_to_twenty_four("9:50 PM") == "21:50"
    
    