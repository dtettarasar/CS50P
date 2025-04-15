import sys

def main():

    file_name = get_arg()

def get_arg():

    print('get arg function')
    
    arg_list = sys.argv
    
    print(arg_list)
    
    if len(arg_list) == 1:
        
        sys.exit('Too few command-line arguments')

main()