import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    
    return check_iframe_format(s)

def check_iframe_format(str):

    if str.startswith("<iframe") and str.endswith("</iframe>"):
        
        return True
    
    else:
        
        return False

if __name__ == "__main__":
    main()
