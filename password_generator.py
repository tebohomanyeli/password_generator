#Password Generator Project (18 October 2022)
#Imported Modules-------------------------------------------------------------
import random


#Global Variables-------------------------------------------------------------
letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 
            'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z', 'A', 'B', 'C', 'D', 
            'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 
            'Q', 'R', 'S', 'T', 'U', 'V', 
            'W', 'X', 'Y', 'Z']
numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [ '!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

#User Inputs:
num_of_letters = int(input("How many letter would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like\n"))
num_of_numbers = int(input("how many numbers would you like\n"))


#Logic and Code---------------------------------------------------------------
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easy_password           = ""

for letter in range(num_of_letters):
    easy_password += f"{letters[random.randint(0, len(letters))-1]}"

for symbol in range(num_of_symbols):
    easy_password += f"{symbols[random.randint(0, len(symbols))-1]}"

for number in range(num_of_numbers):
    easy_password += f"{numbers[random.randint(0, len(numbers))-1]}"

#Output
print(f"Here is your password: {easy_password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total_length_of_password    = num_of_letters + num_of_numbers + num_of_symbols
hard_password               = []
#created counts to ensure that the password doesn't use the characters more times then the user has decided
count_letters               = 0
count_symbols               = 0
count_numbers               = 0

for charaters in range(total_length_of_password):
    
    if len(hard_password) == 0:
        random_index_spot = 0
    else:
        random_index_spot =   random.randint(0,len(hard_password)-1)
    
    random_letter_index   =   random.randint(0,len(letters)-1)
    random_symbol_index   =   random.randint(0,len(symbols)-1)
    random_number_index   =   random.randint(0,len(numbers)-1)

    if count_letters < num_of_letters:
            count_letters += 1
            hard_password.insert(random_index_spot,letters[random_letter_index])
    
    elif count_symbols < num_of_symbols:
            count_symbols += 1
            hard_password.insert(random_index_spot,symbols[random_symbol_index])

    elif count_numbers < num_of_numbers:
            count_numbers   += 1
            hard_password.insert(random_index_spot,numbers[random_number_index])

#Output
print(f"Here is your password: {''.join(hard_password)}")