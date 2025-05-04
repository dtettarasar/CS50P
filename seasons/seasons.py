from datetime import date
import re
import sys

def main():
    
    birth_date = Birthdate()
    
    print(birth_date.user_input)

class Birthdate:
    
    pattern = r"^\b\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b$"
    
    def __init__(self):
        
        self.user_input = Birthdate.ask_date()        
    
    def ask_date():
        
        str = input('Date of Birth: ')
        return str
    
    @property
    def user_input(self):
        return self._user_input
    
    @user_input.setter
    def user_input(self, value):
        
        check_format = re.search(Birthdate.pattern, value)
        #print(check_format)

        if check_format == None:
            sys.exit("Invalid date")
        else:
            self._user_input = value


if __name__ == "__main__":
    main()
