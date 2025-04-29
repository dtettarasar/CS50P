import validators

def main():
    print(verify_email(input("What's your email address? ")))

def verify_email(str):
    
    check_email = validators.email(str)
    
    if check_email == True:
        
        return "Valid"
    
    else:
        
        return "Invalid"
    
if __name__ == "__main__":
    main()