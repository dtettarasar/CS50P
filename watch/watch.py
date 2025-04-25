# About the exercice : https://cs50.harvard.edu/python/2022/psets/7/watch/

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
    
    # print(x)
    # print(x.group(0))
    
    if x:
        
        # return True
        
        src_attribute = x.group(0)
        print(src_attribute)
        
        src_link = re.sub('(src=\")', '', src_attribute)
        src_link = re.sub('(\")', '', src_link)
        
        print(src_link)
        
        
    
    else:
        
        return None



def check_iframe_format(str):

    if str.startswith("<iframe") and str.endswith("</iframe>"):
        
        return True
    
    else:
        
        return False

if __name__ == "__main__":
    main()
