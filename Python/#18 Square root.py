
n = int(input())
l = []
for _ in range(n):
    a = input().split()
    x = int(a[0])
    k = int(a[1])
    r = 1
    for _ in range(k):
        d = x/r
        r = (r+d)/2
    l.append(str(r))
print(' '.join(l))