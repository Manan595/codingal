number1=[1,2,3]
number2=[4,5,6]

results= map(lambda x,y:x+y, number1, number2)
print('addetional of two lists')
print(list(results))

nums= [1,2,3,4,5,67]
def sq(n):
    return n*n
square= list(map(sq,nums))
print('square of numbers in list')
print(square)