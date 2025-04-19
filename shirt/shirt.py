import sys

from PIL import Image

def main():
    
    file_names = get_file_names()
    
    img_file = get_file_content(file_names['input'])
    
    size = img_file.size

    print('img size')
    print(size)
    
    
    
def get_file_names():
    
    # print("init get_file_names function")
    
    valid_format = [
        'jpg',
        'jpeg',
        'png'
    ]
    
    file_names = {
        'input': None,
        'output': None
    }
    
    arg_list = sys.argv
    
    if len(arg_list) <= 2:
        
        sys.exit('Too few command-line arguments')
        
    elif len(arg_list) > 3:
        
        sys.exit('Too many command-line arguments')
     
    file_names['input'] = arg_list[1]
    file_names['output'] = arg_list[2]
    
    print(file_names)
    
    input_format = get_format(file_names['input'])
    output_format = get_format(file_names['output'])
    
    print(f"input_format: {input_format}")
    print(f"output_format: {output_format}")
    
    if input_format == False or input_format not in valid_format:
        
        sys.exit('Invalid input')
        
    if output_format == False or output_format not in valid_format:
        
        sys.exit('Invalid output')
    
    if input_format != output_format:
        
        sys.exit('Input and output have different extensions')
        
    else:
        
        return file_names
        

def get_file_content(input_file_name):
    
    print("init get_file_content function")
    
    print(input_file_name)
    
    try:
        
        img_file = Image.open(input_file_name)        
        
        return img_file
        
    except FileNotFoundError:
        
        sys.exit('Input does not exist')
        
    
# check that str contain one dot. if yes then return what's after the dot to get the file format
def get_format(str):

    # str.count(".") == 1:

    if str.count(".") == 1:
        # print("String format is valid")
        format = str.split(".")
        return format[1]

    elif str.count(".") == 2:
        # print("String format is valid")
        format = str.split(".")
        return format[2]

    else:
        # print("String format is not valid")
        return False
    
main()