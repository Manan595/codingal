def tailrec(n,num):
    if n > num:
        return
    print(n)
    tailrec(n+1,num)

n=int(input('enter n to print 1 to 10 '))

tailrec(1,n)