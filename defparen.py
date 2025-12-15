def paren(s,l,r,p,n):
    if(p==2*n):
        for ss in s:

            print(ss,end='')
        print('\n')
        return
    if(l>r):
        s[p]="}"
        paren(s,l,r+l,p+l,n)
    if (l>n):
        s[p]="}"
        paren(s,l+l,r,p+l,n)
    
n=int(input('enter number of brakets : '))
s=[""]*2*n
print('\n')
paren(s,0,0,0,n)