from datetime import date
import re
import sys
import inflect
p = inflect.engine()

def main():
    
    try:
        str = input('Date of Birth: ')
        
        birth_date = Birthdate(str)
        # birth_date.get_age_in_min()
        # print(birth_date.age_in_min)
        print(birth_date.get_age_in_words_min())
    
    except ValueError:
        
        sys.exit("Invalid date")
        
    # print(birth_date)


class Birthdate:
    
    pattern = r"^\b\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b$"
    
    def __init__(self, str):
        
        self.user_input = str
        Birthdate.get_age(self)
        Birthdate.get_age_in_min(self)    
    
    def __str__(self):
        return 'date to be converted here'
    
    def get_age(self):
        
        # print('init get_age method')
        
        # print(f"birth date is equal to: {self.user_input}")
        
        self.date_value = date.fromisoformat(self.user_input)
        # print("date value")
        # print(self.date_value.ctime())
        
        today = date.today()
        
        self.age = today - self.date_value
        # print(self.age)
        
    def get_age_in_min(self):
        
        # print('init get_age_in_min method')
        
        self.age_in_min = int(self.age.total_seconds() / 60)
        
    def get_age_in_words_min(self):
        
        age_words = p.number_to_words(self.age_in_min, andword="")
        
        return f"{age_words.capitalize()} minutes"
        
    @property
    def age_in_min(self):
        return self._age_in_min
    
    @age_in_min.setter
    def age_in_min(self, value):
        self._age_in_min = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        
        self._age = value
        
    @property
    def date_value(self):
        return self._date_value
    
    @date_value.setter
    def date_value(self, value):
        
        self._date_value = value
    
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
