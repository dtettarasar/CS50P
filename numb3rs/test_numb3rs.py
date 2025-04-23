from numb3rs import validate

def test_valid_addresses():
    
    assert validate('127.0.0.1') == True
    assert validate('512.512.512.512') == True
    