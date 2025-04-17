import sys
import csv

def main():
    
    print("init main function")
    
    file_names = get_file_names()
    
    print(file_names)
    
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
        
    file_names['input'] = arg_list[1]
    file_names['output'] = arg_list[2]
    
    # print(file_names)
    
    if file_names['input'].endswith(".csv") == False or file_names['output'].endswith(".csv") == False:
        
        sys.exit("input and output files should be in CSV format")
        
    else:
        
        return file_names
    
    
def get_file_content(input_file_name): 
    
    print("init get_file_content function")
    
def build_output_file(file_content):
    
    print("init build_output_file function")

main()