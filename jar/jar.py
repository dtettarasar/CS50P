
class Jar:
    def __init__(self, capacity=12):
        
        self.capacity = capacity
        self.stored_cookies = 0

    def __str__(self):
        return "🍪"

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...
        
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
    def stored_cookies(self):
        return self._stored_cookies
    
    @stored_cookies.setter
    def stored_cookies(self, value):
        self._stored_cookies = value

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, value):
        
        # check if the value is in string format
        
        self._capacity = self.value_check(value)
        

    @property
    def size(self):
        ...