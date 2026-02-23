a = [0,1,2,2,1,0,1,0,2,1,1,0,2,1,0,1,0]
zeros = []
ones = []
twos = []
new = []

for i in range(0, len(a)):
    if a[i] == 0:
        zeros.append(a[i])
    elif a[i] == 1:
        ones.append(a[i])
    elif a[i] == 2:
        twos.append(a[i])

for i in range(0, len(zeros)):
    new.append(zeros[i])

for i in range(0, len(ones)):
    new.append(ones[i])

for i in range(0, len(twos)):
    new.append(twos[i])

print("Old array:\n", a, "\nThe new array with zeros at the end looks like this:\n", new)