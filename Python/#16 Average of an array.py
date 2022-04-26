import math
n = int(input())
k = []
for _ in range(n):
    a = input().split()
    y = 0
    total= []
    for x in a:
        if int(x) != 0:
            total.append(x)
        y += int(x)
    u = math.floor(((y/len(total)))+0.5)
    k.append(str(u))
print(' '.join(k))
        