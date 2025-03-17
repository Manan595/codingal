import random
import string 

print("herllo, Welcome to password generator ")
lenght = int(input("Enter The lenght of the password ")) 
lower= string.acsii_lowercase
upper=string.acsii_uppercase
num = string.digits
symbols=string.punctuation

all= lower+upper+num+symbols

temp=random.sample(all,lenght)

password="".join(temp)