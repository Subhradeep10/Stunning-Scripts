import random
import array

x="y"
while x=="y":
    max_len=int(input("Enter the lenght of the password you want : "))
    if max_len >= 8:
        digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        lower_case=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
        
        upper_case=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        
        symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', ':', '?', '.', '/', '|', '~', '>', '<']
        
        mix = digits + upper_case + lower_case + symbols
        
        random_digit = random.choice(digits)
        random_upper = random.choice(upper_case)
        random_lower = random.choice(lower_case)
        random_symbol = random.choice(symbols)
        
        temp_pass = random_digit + random_upper + random_lower + random_symbol
        
        for x in range(max_len - 4):
            temp_pass = temp_pass + random.choice(mix)
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
            
        password = ""
            
        for x in temp_pass_list:
            password = password + x
                
        print(password,"\n")

    else:
        print("Password length should be of minimum 8 characters\n")

    x=input("Do you want another password (y/n) : ")