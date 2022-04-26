n = int(input())
l= []
for x in range(n):
    j = input().split()
    a = int(j[0])
    b = int(j[1])
    c = int(j[2])
    if a > b and a > c:
        if b > c:
            l.append(str(b))
        else:
            l.append(str(c))
    elif b > a and b > c:
        if a > c:
            l.append(str(a))
        else:
            l.append(str(c))
    else:
        if a > b:
            l.append(str(a))
        else:
            l.append(str(b))
    

print(' '.join(l))