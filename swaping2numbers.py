def swap4(a,b):
    a=a^b
    b=a^b
    a=a^b
    print('After swaping: a =', a,'b =',b)

def swap5(a,b):
    a-(a&b)+ (a|b)
    b=a+(~b)+1
    a=a+(~b)+1
    
    print('after swaping:a =',a,'b=',b)

swap4(1,2)
swap5(2,1)