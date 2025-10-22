def reversebits(number):
    reversed=0

    while (number>0):
        reversed=reversed<<1
        
        if (number&1==1):
            reversed=reversed^1

        number = number>>1

    return reversed
number=int(input('enter your number'))
print('number with reversed bits',reversebits(number))