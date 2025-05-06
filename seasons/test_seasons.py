import pytest
from seasons import Birthdate

def test_valid_date():
    
    birth_date = Birthdate("2024-05-06")
    assert birth_date.get_age_in_words_min() == "Five hundred twenty-five thousand, six hundred minutes"
    
def test_invalid_date():
    
    with pytest.raises(ValueError):
        birth_date = Birthdate("2024-56-62")
