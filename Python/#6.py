import math
n = int(input())
j = []
for x in range(n):
    i = input().split()
    for a in range(0,1):
        c = float(i[a]) 
    for b in range(1,2):
        e = float(i[b])
    f = math.floor(c/e +0.5)
    j.append(str(f))
print(' '.join(j))
