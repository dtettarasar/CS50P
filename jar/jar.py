
class Jar:
    def __init__(self, capacity=12):
        
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self._size*"🍪"

    def deposit(self, n):
        
        self.size = self.size + n
        
    def withdraw(self, n):
        
        self.size = self.size - n
        
        
    def value_check(self, value):
        
         # check if the value is in string format
         
         if isinstance(value, str) and value.isdigit() == False:
             
             raise ValueError('make sure the value provided is a valid integer')
         
         elif isinstance(value, str) and value.isdigit() == True:
             
             value = int(value)
             
         if value > 0:
             
             return value
         
         else:
            
            raise ValueError('make sure the value provided is a positive integer')    
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        self._size = value

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, value):
        
        self._capacity = self.value_check(value)
        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        
        if value > self.capacity:
            
            raise ValueError("cookie jar’s capacity exceeded")
        
        elif value < 0:
            
            raise ValueError("too much cookies withdrawn")
        
        else:
        
            self._size = value