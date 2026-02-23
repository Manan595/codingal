def getmaxlenght(a,a_size):

    conter = 0
    maxones = 0

    for i in range(0, a_size):
        if (a[i]==0):
            conter = 0
        

        else:
            conter += 1
            maxones = max(maxones,conter)
        return maxones
a=[1,1,0,0,1,0,1,0,1,1,1,1]
a_size=len(a)

print('maxs 1s is ',getmaxlenght(a,a_size))