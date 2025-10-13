def checkfsame(number1,number2):
    if ((number1 ^ number2)!=0):
      print('number are not equal')
    else:
       print('the number are equal')

number1=int(input('enter your first number'))
number2=int(input('enter your second number'))

checkfsame(number1,number2)