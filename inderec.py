def indrec(n,num):
    if(n<1 or n>num ):
        return
    print(n)
    indrec(n-1,num)
    print(n)
n=int(input('enter the value of n to print 1 to 10'))
indrec(n,n)