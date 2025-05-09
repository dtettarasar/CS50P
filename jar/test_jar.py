import pytest
from jar import Jar
    
def test_init_class():
    
    # test with an int
    jar_one = Jar(10)
    assert jar_one.capacity == 10
    
    # test with a string
    jar_two = Jar('12')
    assert jar_two.capacity == 12
    
def test_invalid_capacity():
    
    with pytest.raises(ValueError):
        
        jar = Jar("not an int")
        
    with pytest.raises(ValueError):
        
        jar = Jar(-5)
        
    with pytest.raises(ValueError):
        
        jar = Jar('-8')
        
    with pytest.raises(ValueError):
        
        jar = Jar(0)
        
    