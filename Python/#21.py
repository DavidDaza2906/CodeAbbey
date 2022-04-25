n = input().split()
a = input().split()
data = int(n[0])
k = []
numbers = list(range(int(n[1])+1))
for x in numbers:
    counter = 0
    for y in a:
        y = int(y)
        if y ==x:
            counter +=1
    if counter != 0:
        k.append(str(counter))
print(' '.join(k))