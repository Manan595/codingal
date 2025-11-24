def tailhead(n,num):
    if n >num:
        return
    print(n)
    tailhead(n+1,num)
def headtail(n,num):
    if n>num:
        return
    headtail(n+1,num)
    print(n)
n=int(input('enter the number to print number of 1 to 10 then 10 to 1 '))
headtail(1,n)
tailhead(1,n)