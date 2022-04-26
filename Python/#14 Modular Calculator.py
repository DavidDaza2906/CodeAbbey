x = int(input())
k = []
r = True
while r==True:
    a = input().split()
    k.append(a)
    if a[0] == '%':
        r = False
for y in k:
    sign = y[0]
    value = int(y[1])
    if sign == '+':
        x += value
    elif sign == '*':
        x *=value
    else:
        x %= value
print(x)