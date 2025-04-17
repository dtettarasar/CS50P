import sys
import csv

def main():
    
    print("init main function")
    
    file_names = get_file_names()
    
    # print(file_names)
    
    file_content = get_file_content(file_names['input'])
    
    # print(file_content)
    
    build_output_file(file_content, file_names['output'])
    
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
    
    print(input_file_name)
    
    file_content = []
    
    reader = None
    
    try:
        
        with open(input_file_name, newline='') as csvfile:
            
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                
                # print(row)
                # print(row['name'])
                
                name_list = row['name'].split(', ')
                # print(name_list)
                
                row['first'] = name_list[1]
                row['last'] = name_list[0]
                
                del row['name']
                
                file_content.append(row)
                # print(row)
                
                # print('---------------------')
            
            # print(file_content)
            
            return file_content
            
    except FileNotFoundError:
        
        sys.exit('File does not exist')
    
    
def build_output_file(file_content, output_file_name):
    
    print("init build_output_file function")
    
    print(file_content)
    
    keys = file_content[0].keys()
    
    
    with open(output_file_name, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(file_content)

main()