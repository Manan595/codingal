import math;
def printPowerSet (set,SetSize):
    PowerSetSize = (int) (math.pow(2, SetSize))
    outer = 0
    inner = 0
    
    for outer in range (0,PowerSetSize):
        for inner in range(0,SetSize):
            if((outer & (1<<inner))> 0):
                print(set[inner], end = "")
        print("")

size=int(input('enter array size'))
set=[]
for i in range(0,size):
    n = int(input('enter element'))
    set.append(n)

printPowerSet(set,len(set))