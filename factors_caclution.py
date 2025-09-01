def print_factors(number):
    print("the factors of",number,"are:")
    for i  in range(1,number):
        if number % i ==0:
            print(i)
number= int(input("enter your number find it's factors"))
print_factors(number)