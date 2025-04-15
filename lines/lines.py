import sys

def main():

    file_name = get_arg()

def get_arg():

    print('get arg function')
    
    arg_list = sys.argv
    
    print(arg_list)
    
    if len(arg_list) == 1:
        
        sys.exit('Too few command-line arguments')
        
    elif len(arg_list) > 2:
        
        sys.exit('Too many command-line arguments')
        
    file_name = arg_list[1]
    print(file_name)
    
    if file_name.endswith(".py") == False:
        
        sys.exit('Not a Python file')

main()