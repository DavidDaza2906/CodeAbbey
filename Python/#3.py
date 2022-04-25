a = int(input())
b = []
for c in range(a):
    d = 0
    e = input().split()
    for f in range(0,2):
        d += int(e[f])
    b.append(str(d))
print(' '.join(b))