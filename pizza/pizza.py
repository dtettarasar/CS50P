import sys
import csv

from tabulate import tabulate

def main():
    
    file_name = get_file_name()
    
    file_content = get_file_content(file_name)
    
    table = build_table(file_content)
    
    print(table)
    
    # table = [["Sun",696000,1989100000],["Earth",6371,5973.6], ["Moon",1737,73.5],["Mars",3390,641.85]]
    # print(tabulate(table))
    
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

def get_file_content(file_name):
    
    # print('init get file content')
    # print(file_name)
    
    file_content = []
    
    reader = None
    
    try:
        
        with open(file_name, newline='') as csvfile:
            
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                
                file_content.append(row)
            
            # print(file_content)
            
            return file_content
            
    except FileNotFoundError:
        
        sys.exit('File does not exist')
        
        
def build_table(file_content):
        
    header = file_content[0].keys()
    rows =  [x.values() for x in file_content]
    
    return tabulate(rows, header, tablefmt='grid')
    
    
main()