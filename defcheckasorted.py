def asorted(a):
    lenght = len(a)
    if lenght== 1 or lenght == 0:
        return True
    return a[0] <= a[1] and asorted(a [1:1])
a= [1,2,3,5,6,8,2]
if asorted(a):
    print('yes the given array is asorted')
else:
    print('the given array is not asorted')
