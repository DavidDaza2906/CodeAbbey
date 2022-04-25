n = int(input())
c = []
for x in range(n):
    a = input().split()
    for j in range(0,1):
        b = int(a[j])
    for g in range(1,2):
        e = int(a[g])
    if b > e:
        c.append(str(b))
    else:
        c.append(str(e))
print(' '.join(c))