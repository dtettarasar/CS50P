class Jar:
    def __init__(self, capacity=12):
        
        self.capacity = capacity

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, value):
        
        # check if the value is in string format
        
        if isinstance(value, str) and value.isdigit() == False:
            
            raise ValueError('make sure the capacity provided is a valid integer')
        
        elif isinstance(value, str) and value.isdigit() == True:
            
            value = int(value)
            
        if value > 0:
            
            self._capacity = value
            
        else:
            
            raise ValueError('make sure the capacity provided is a positive integer')    
        
        

    @property
    def size(self):
        ...