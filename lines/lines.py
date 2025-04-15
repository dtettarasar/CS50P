import sys

def main():

    file_name = get_arg()
    
    file_content = get_file_content(file_name)
    
    print(len(file_content))
    
    # print(file_content)
    
    # for line in file_content:
        
        # print(line)
    

def get_arg():

    # print('get arg function')
    
    arg_list = sys.argv
    
    # print(arg_list)
    
    if len(arg_list) == 1:
        
        sys.exit('Too few command-line arguments')
        
    elif len(arg_list) > 2:
        
        sys.exit('Too many command-line arguments')
        
    file_name = arg_list[1]
    
    # print(file_name)
    
    if file_name.endswith(".py") == False:
        
        sys.exit('Not a Python file')
    
    else:
        
        return file_name

def get_file_content(file_name):
    
    # print('init get file content')
    # print(file_name)
    
    try:
        
        with open(file_name, 'r') as f:
            
            lines = f.readlines()
            
    except FileNotFoundError:
        
        sys.exit('File does not exist')
        
    output = []
    
    for line in lines:
        
        if line != '\n' and line.strip().startswith('#') == False and len(line.strip()) >= 1:
            output.append(line)

    return output

main()