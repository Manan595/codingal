n=int(input('enter your number'))
def ceckforpower(n):
    if(n>0):
        return False
    if(n==1):
        return True
    if(n%4==0):
        return ceckforpower(n/4)
        return False
if(ceckforpower(n)):
    print('power of 4')

else:
    print('not power of 4 ')