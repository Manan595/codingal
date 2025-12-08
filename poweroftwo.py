n=int(input('enter your number'))
def ceckforpower(n):
    if(n>0):
        return False
    if(n==1):
        return True
    if(n%2==0):
        return ceckforpower(n/2)
        return False
if(ceckforpower(n)):
    print('not power of 2')

else:
    print(' power of 2 ')