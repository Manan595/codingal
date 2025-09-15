from math import sqrt
number=int(input('enter the number you want to check for prime:'))
if number > 1:
    for i in range(2, int(sqrt(number))+1):
        if (number %i)==0:
            print('number is not a prime number')
            break
    else:print('the number is a prime number ')

else:print('the number is not a prime number')