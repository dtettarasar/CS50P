from datetime import date
import re
import sys

def main():
    
    try:
    
        birth_date = Birthdate()
    
    except ValueError:
        
        sys.exit("Invalid date")
        
    # print(birth_date)


class Birthdate:
    
    pattern = r"^\b\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b$"
    
    def __init__(self):
        
        self.user_input = Birthdate.ask_date()
        Birthdate.convert_to_int(self)        
    
    def ask_date():
        
        str = input('Date of Birth: ')
        return str
    
    def __str__(self):
        return 'date to be converted here'
    
    def convert_to_int(self):
        
        print("init convert to minutes method")
        print(f"birth date is equal to: {self._user_input}")
        
        date_elem_list = self._user_input.split('-')
        print(date_elem_list)
        
        self.year = date_elem_list[0]
        
        print(self.year)
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        
        try:
            
            self._year = int(value)
        
        except:
            
            ValueError('year not valid')
    
    @property
    def user_input(self):
        return self._user_input
    
    @user_input.setter
    def user_input(self, value):
        
        check_format = re.search(Birthdate.pattern, value)
        #print(check_format)

        if check_format == None:
            # sys.exit("Invalid date")
            raise ValueError
        else:
            self._user_input = value


if __name__ == "__main__":
    main()
