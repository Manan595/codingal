s1={2,3,1}
s2={'c','b','c'}
s3=list(zip(s1,s2))

list1=[10,20,30,40]
list2=[100,200,300,400]

for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks=['relience','infosys','tcs']
prices=[2175,1127,2750]

new_dict={stocks:prices for stocks,
          prices in zip (stocks,prices)}
print(format(new_dict))