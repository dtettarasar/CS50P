import sys

def main():
    
    file_name = get_file_name()
    
    print(file_name)
    
def get_file_name():

    # print('get arg function')
    
    arg_list = sys.argv
    
    # print(arg_list)
    
    if len(arg_list) == 1:
        
        sys.exit('Too few command-line arguments')
        
    elif len(arg_list) > 2:
        
        sys.exit('Too many command-line arguments')
        
    file_name = arg_list[1]
    
    # print(file_name)
    
    if file_name.endswith(".csv") == False:
        
        sys.exit('Not a CSV file')
    
    else:
        
        return file_name
    
main()