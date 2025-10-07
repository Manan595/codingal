def firstsetbit(number):
    postion=1
    mask=1
    while (not(number&mask)):
        mask=mask<<1
        postion+= 1 


    return postion
number= int(input('enter number'))

print('postions of the first set bit ',firstsetbit(number))