def equilibriumpoint(arr):
    leftsidesum=0
    rightsidesum=0
    n= len(arr)

    for i in range(n):
        leftsidesum=0
        rightsidesum=0

        for j in range(i):
            leftsidesum+=arr[j]
        for j in range(i+1,n):
            rightsidesum+=arr[j]
        
        if leftsidesum == rightsidesum:
            return i
    return -1
arr=[-4,6,2,0,0,1,1]
print('element :',arr[equilibriumpoint(arr)])