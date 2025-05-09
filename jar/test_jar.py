import pytest
from jar import Jar
    
def test_init_class():
    
    # test with an int
    jar_one = Jar(10)
    assert jar_one.capacity == 10
    assert jar_one.stored_cookies == 0
    
    # test with a string
    jar_two = Jar('12')
    assert jar_two.capacity == 12
    assert jar_two.stored_cookies == 0
    
def test_invalid_capacity():
    
    with pytest.raises(ValueError):
        
        jar = Jar("not an int")
        
    with pytest.raises(ValueError):
        
        jar = Jar(-5)
        
    with pytest.raises(ValueError):
        
        jar = Jar('-8')
        
    with pytest.raises(ValueError):
        
        jar = Jar(0)
        
def test_str_method():
    
    jar = Jar(5)
    
    assert jar.__str__() == "🍪"
    
def test_deposit_method():
    
    jar = Jar(10)
    
    jar.deposit(5)
    
    assert jar.stored_cookies == 5
    
    with pytest.raises(ValueError):
        
        jar.deposit(20)