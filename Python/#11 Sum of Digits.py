import math
n = int(input())
b = []
for x in range(n):
    a = input().split()
    for y in a:
        q = int(a[0])
        r = int(a[1])
        f = int(a[2])
        h = (q*r)+f
        c= 0
        k = -1
    while k < c :
        k = c
        h = int(h)
        t = math.floor(h%10)
        h = h/10
        c += t
        if k == c:
            b.append(str(c))
            c = k-1
    
print(b)
            
        