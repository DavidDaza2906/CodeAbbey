n = int(input())
c = []
for x in range(n):
    a = input().split()
    for j in range(0,1):
        b = int(a[j])
    for g in range(1,2):
        e = int(a[g])
    for h in range(2,3):
        f = int(a[h])
    if b > e:
        b = a
    if b < c:
        c=b
print(' '.join(c))
#b = 1
# 