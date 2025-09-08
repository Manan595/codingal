def isplindrome(string):

    reversedstring=''.join(reversed(string))

    if string == reversedstring:
        return True
    else:
        return False
    
string = input('enter the string')
ans = isplindrome(string)

if (ans):
    print('yes',string,'is a palindrome')
else:
    print('no',string,'is not a palindrome')