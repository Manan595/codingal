def o1(n,m):
    total=n*m
    print('\n number of iteration is 1')


def On(n,m):
    total = 0
    for i in range (1,n+1):
        total+=m
    print('N iterations',n)


m=int(input("enter 'a'for a+b : "))
n=int(input("enter'b' for a+b : "))

o1(m,n)
On(m,n)