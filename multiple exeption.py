try:
    num1, num2=eval(input("enter two numbers with comma in the middle "))
    result=num1/num2
except ZeroDivisionError:
 print("Divsion by zero is an error")

except SyntaxError:
 print("comma missing, enter numbers with a commaa in the middle ")

except:
 print("wrong input ")

else:
 print(" no exeception")

finally:
 print("print this will execute no matter what ")