def totalsum(a):
    lenght = len(a)
    if lenght == 1:
        return a[0]
    return a[0]+ totalsum(a[1:])
a=[1,2,3,6,3,4,5,6,7,8,5,6,7,3]
print('the total sum is ',totalsum(a))
