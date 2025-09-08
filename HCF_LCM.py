numberlargest=int(input('enter the largest number '))
numebersmallest=int(input('enter the smallest number'))
a=numberlargest
b=numebersmallest

while(numebersmallest):
    numberstore=numebersmallest
    numebersmallest=numberlargest%numebersmallest
    numberlargest=numberstore

print('hcf is :', numberlargest)
l=(a*b)/numberlargest
print('lcm is : ', l)