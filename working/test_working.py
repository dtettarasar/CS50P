from working import check_input

def test_valid_input():
    
    assert check_input("9 AM to 5 PM") == True
    
def test_invalid_input():
    
    assert check_input("9 AM - 5 PM") == False