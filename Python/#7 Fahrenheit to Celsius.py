n = int(input())
a = input().split()
f = []
for x in range(n):
    b = round((int(a[x])-32)*5/9)
    f.append(str(b))
print(' '.join(f))
    