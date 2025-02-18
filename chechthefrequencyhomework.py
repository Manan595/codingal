tec={'codingal':3,'is':3,'the':3,'best':3}
print('the original dictonary'+ str (tec ))

k=int(input('enter a number '))

res=0
for key in tec:
    if tec[key]==k:
        res=res+1
print('frequency of k is :'+str(res))        