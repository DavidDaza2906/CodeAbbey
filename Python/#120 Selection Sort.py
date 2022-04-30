

n = int(input())
a = input().split()
a = [int(x) for x in a]
index = []
for _ in range(n):
    maxm = max(a)
    maxPosition = a.index(maxm)
    a[maxPosition] = a[n-1]
    a[n-1] = maxm
    a.pop(n-1)
    n -= 1
    if len(a) > 0:
        index.append(str(maxPosition))

print(' '.join(index))