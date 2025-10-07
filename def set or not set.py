def setornot(number,n):
    if number &(1<<(n-1)):
        print('set')
    else: 
        print('not set')

number=int(input('enter number:'))
n=int(input('enter bit number'))
setornot(number,n)