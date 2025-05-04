from datetime import date
import re
import sys

def main():
    
    input = Birthdate()
    
    print(input.birth_date)

class Birthdate:
    
    pattern = r"\b\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b"
    
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
        
        check_format = re.search(Birthdate.pattern, value)
        #print(check_format)

        if check_format == None:
            sys.exit("Invalid date")
        else:
            self._birth_date = value



if __name__ == "__main__":
    main()
