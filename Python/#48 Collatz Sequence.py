n = int(input())
a = input().split()
k = []
for x in a:
    x = int(x)
    r = True
    count = 0
    while r == True:
        if x%2 == 0:
            x = x/2
        else:
            x = 3*x+1
        count +=1
        if x == 1:
            k.append(str(count))
            r = False
print(' '.join(k))