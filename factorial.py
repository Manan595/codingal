def fac(n):
    if (n==1 or n==0):
        return 1 
    return n*fac(n-1)
n=int(input("enter your nuber"))
print("factorial of ", n,'is',fac (n))

print('the time complexity of recursive funtions is O(nlogn)')