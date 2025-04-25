import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    
    is_iframe =  check_iframe_format(s)
    
    if is_iframe == False:
        
        sys.exit("make sure you provide an iframe HTML element")
        
    # print(s)
    
    src_regex = 'src=\"https?:\/\/w?w?w?\.?youtube.com\/embed\/\w+\"'
    
    x = re.search(src_regex, s)
    
    print(x)

def check_iframe_format(str):

    if str.startswith("<iframe") and str.endswith("</iframe>"):
        
        return True
    
    else:
        
        return False

if __name__ == "__main__":
    main()
