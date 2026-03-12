#imports 

import secrets 
import string

#start of the code 

#strings

letters = string.ascii_letters
numbers = string.digits

characters = letters + numbers

#creating groups

def generate_password():

    groups = []
    count = 0

    while count < 3:
        group = ""
        count2 = 0

        while count2 < 4:
            character = secrets.choice(characters)
            group += character
        
            count2 += 1

        groups.append(group)
    
        count += 1

#joins the 3 groups together to make the final password

    password = "-".join(groups)

    print("Please enter your code to access your password.")
    check = str(input("Input : "))

    #just made it 1111 for now 

    if check == "1111":
        print(password)

    else:
        print("Invalid code.")

generate_password()
    