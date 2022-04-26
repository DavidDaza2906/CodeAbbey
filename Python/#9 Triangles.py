def triangulo():
    if a +b > c:
        if b+c > a:
            if c+a > b:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0 
    
n = int(input())
k = []
for x in range(n):
    l = input().split()
    a = int(l[0])
    b = int(l[1])
    c = int(l[2])
    k.append(str(triangulo()))
print(' '.join(k))