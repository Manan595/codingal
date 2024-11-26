def enterage(age):
    if age < 0:
     raise ValueError("only positivev intigers allowed ")
    if age%2 ==0:
       print ("age is even")
    else:
       print("age is odd")
try:
   num = int(input("enter your age "))
except ValueError:
   print("only positive numbers allowed ") 

except:
   print("something is wrong ")   
