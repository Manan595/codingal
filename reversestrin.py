def reversestring(s):
    if len(s)==1:
        return s[0]
    firstchair= s[0]
    return reversestring (s[1:])+firstchair
s='manan patel'
print(reversestring(s))