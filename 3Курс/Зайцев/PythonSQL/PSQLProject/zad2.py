a = str(input())
xo = a[0]
c = 0
for x in a:
    if x in xo:
        c += 1
    else:
        print(xo + str(c), end='')
        xo = x
        c = 1
print(xo + str(c), end='')

s = str(input())
s0 = s[0]
i = 0
for x in s:
    if x in s0:
        i += 1
    else:
        print(s0 + str(i), end='')
        s0 = x
        i = 1
print(s0 + str(i), end='')
