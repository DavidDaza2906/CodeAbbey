

a = input().split()
c = len(a)-1
b = []
swaps = 0
for _ in range(c):
    x = int(a[0])
    y = int(a[1])
    if y != -1:
        if x <y:
            b.append(x)
            a.pop(0)
        else:
            b.append(y)
            a[1] = x
            a.pop(0)
            swaps +=1
    else:
        b.append(x)    
def checksum(b):
    result = 0
    for x in b:
        result += x
        result *=113
    result %= 10000007
    return result
print(swaps, checksum(b) )

    