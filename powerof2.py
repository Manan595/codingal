def power2(number):
    if (number==0):
        return 0
    if ((number& (~(number -1)))== number):
        return 1
    return 0
number = int(input('enter the number'))

if (power2(number)):
    print('the number is power of 2 ')
else:
    print('the number is not power of 2 ')