def maxelement(a):
    lenght= len(a)
    if lenght == 1:
        return a[0]
    return max (a[0],maxelement(a[1:]))
a= [1,2,345,678,743,1,8]
print(' the largest element of the array',maxelement(a))
