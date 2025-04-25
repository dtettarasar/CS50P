import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    
    return check_iframe_format(s)

def check_iframe_format(str):

    if str.startswith("Hello") and str.endswith('World'):
        
        return True
    
    else:
        
        return False

if __name__ == "__main__":
    main()
