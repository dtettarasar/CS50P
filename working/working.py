import re
import sys


def main():
    
    print(convert(input("Hours: ")))
    
    # print(check_input("9 AM to 5 PM"))
    
    ...


def convert(s):
    
    s_is_valid = check_input(s)
    
    if s_is_valid == False:
        
        raise ValueError('input is invalid')
        
        # print('input is invalid')
    
    else:
        
        print('input is valid')

    
...

def check_input(str):
    
    # print("init check input")
    # print(str)
    
    regex = r"^(1[0-2]|[1-9])(\s{1}|(:{1}[0-5][0-9])?\s)(AM|PM)(\sto\s)(1[0-2]|[1-9])(\s{1}|(:{1}[0-5][0-9])?\s)(AM|PM)$"
    
    input_is_valid = re.search(regex, str)
    
    if input_is_valid:
        
        return True
    
    else: 
        
        return False


if __name__ == "__main__":
    main()
