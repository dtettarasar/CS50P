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
        self.month = date_elem_list[1]
        self.day = date_elem_list[2]
        
        print(f'year: {self.year}')
        print(f'month: {self.month}')
        print(f'day: {self.day}')
    
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        
        try:
            
            self._year = int(value)
        
        except ValueError:
            
            print('year not valid')
    
    
    @property
    def month(self):
        return self._month
    
    @month.setter
    def month(self, value):
        
        try:
            
            self._month = int(value)
            
        except ValueError:
            
            print('month not valid')
    
    
    @property
    def day(self):
        return self._day
    
    @day.setter
    def day(self, value):
        
        try:
            
            self._day = int(value)
            
        except ValueError:
            
            print('day not valid')
    
    
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
