k = input().split()
j = []
for x in k:
    x =x[::-1]
    j.append(x)
j =j[::-1]
print(' '.join(j))