import sys
import csv

def main():
    
    print("init main function")
    
    file_name = get_file_names()
    
def get_file_names():
    
    print("init get_file_names function")
    
    file_names = {
        'input': None,
        'output': None
    }
    
    arg_list = sys.argv
    
    if len(arg_list) == 1:
        
        sys.exit('Too few command-line arguments')
        
    elif len(arg_list) > 3:
        
        sys.exit('Too many command-line arguments')
    
def get_file_content(file_name): 
    
    print("init get_file_content function")
    
def build_output_file(file_content):
    
    print("init build_output_file function")

main()