import pytest
from jar import Jar
    
def test_init_class():
    
    # test with an int
    jar_one = Jar(10)
    assert jar_one.capacity == 10
    assert jar_one.size == 0
    
    # test with a string
    jar_two = Jar('12')
    assert jar_two.capacity == 12
    assert jar_two.size == 0
    
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
    
    jar.deposit(3)
    
    assert jar.__str__() == "🍪🍪🍪"
    
def test_deposit_method():
    
    jar = Jar(10)
    
    jar.deposit(5)
    
    assert jar.size == 5
    
    with pytest.raises(ValueError):
        
        jar.deposit(20)
        
def test_withdraw_method():
    
    jar = Jar(10)
    
    jar.deposit(5)
    
    jar.withdraw(3)
    
    assert jar.size == 2
    
    jar.withdraw(2)
    
    assert jar.size == 0
    
    with pytest.raises(ValueError):
        
        jar.withdraw(3)