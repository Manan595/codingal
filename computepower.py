def computepower(x,y):
    result=1

    while(y>0):
        if (y%2==0):
            x=x*x
            y>>=1
        else:
            result=result*x
            y=y-1

    return result
x=int(input('enter x for x^y'))
y = int(input('enter y for x^y'))
print('total: ',(computepower(x,y)))