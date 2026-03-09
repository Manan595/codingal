a=[0,1,1,0,0,0,0,1]
zeroflip =0
oneflip = 0
for i in range(len(a)):
    if a[i]==0:
        zeroflip +=1
    if a[i]==1:

        oneflip+=1 
print('It will take',zeroflip,"flips to change all valvues to one \n it will",oneflip,"flip to change all valcues to zero")
