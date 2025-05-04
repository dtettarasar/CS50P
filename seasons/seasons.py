from datetime import date


def main():
    
    input = Birthdate('test')
    
    print(input.birth_date)

class Birthdate:
    
    def __init__(self, birth_date):
        
        self.birth_date = birth_date        
    
    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value    



if __name__ == "__main__":
    main()
