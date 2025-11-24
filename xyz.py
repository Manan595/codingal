def xyz(n):
    n = int(input('enter a number '))
    if n>0:
        print('possitive number')
        xyz(n)

    elif(n==0):
        print('zero')
        xyz(n)
    
    else:
        print('negitive number')

xyz(9)
