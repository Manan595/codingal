number=int(input("input your number"))
digits=len(str(number))
result_number=0
temp=number
while temp > 0:
    digit= temp%10
    result_number += digit ** digit
    temp//=10

if number ==result_number:
    print("number is a armtrong number ")

else:
    print("it is not a armstrong number ")