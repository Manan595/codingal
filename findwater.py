def findwater(a, a_size):
    lefttallest=[0]*a_size
    righttallest=[0]*a_size
    water=0
    lefttallest[0]=a[0]
    for i in range(1,a_size):
        lefttallest[i]=max(lefttallest[i-1],a[i])
    righttallest[0]=a[0]
    for i in range(1,a_size):
        righttallest[i]=max(righttallest[i+1],a[i])
    for i in range(0, a_size):
        water+= min(lefttallest[i],righttallest[i] - a[i])
    return water
a= [0,1,0,2,1,1,0,1,3,2,1,2,1]


