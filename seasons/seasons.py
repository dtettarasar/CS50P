from datetime import date


def main():
    
    input = Birthdate()
    
    print(input.birth_date)
    # print(Birthdate.regex)

class Birthdate:
    
    regex = 'regex'
    
    def __init__(self):
        
        self.birth_date = Birthdate.ask_date()        
    
    def ask_date():
        
        str = input('Date of Birth: ')
        return str
    
    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value):
        # print(Birthdate.regex)
        self._birth_date = value



if __name__ == "__main__":
    main()
