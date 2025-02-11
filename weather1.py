weather=(1,0,0,0,1,1,0)
sunny=0
raniny=0
for i in range(0,7):
    if(weather[i]==0):
         raniny+=1  
else:
    sunny+=1

if (sunny > raniny):
        print("good weather ")
else:
     print("bad weather ")