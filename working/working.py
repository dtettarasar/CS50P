# about the exercice: https://cs50.harvard.edu/python/2022/psets/7/working/
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
        #print(s)
        
        full_time = s.split("to")
        print(full_time)
        
        start_time = full_time[0].strip()
        end_time = full_time[1].strip()
        
        print(f"start_time: {start_time}")
        print(f"end_time: {end_time}")
        
        format_to_twenty_four(start_time)
        format_to_twenty_four(end_time)

    
def format_to_twenty_four(time_str):
    
    hours = 0
    minutes = 0
    
    print('init the format to 24 hour format function')
    print(f"time str: {time_str}")
    
    time_list = time_str.split(' ')
    
    if time_list[0].count(':') == 1:
        
        time_list[0] = time_list[0].split(":")
        
        hours = int(time_list[0][0])
        minutes = int(time_list[0][1])
        
    else:
        
        hours = int(time_list[0])
    
    if hours == 12 and time_list[1] == "AM":
        
        hours = 0
        
    elif time_list[1] == "PM" and hours != 12:
        
        hours += 12
        
        
    print(time_list)
    print(f"hours: {hours}")
    print(f"minutes: {minutes}")
    
    final_str = f'{hours:02d}:{minutes:02d}'
    print(f"final_str: {final_str}")
    
    return final_str
    

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
