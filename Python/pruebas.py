

n = int(input())
a = input().split()
index = []
print(a)
maximo = max(a)

for _ in range(n):
    for x in a:
        
    maxm = max(a)
    #print('maximo', maxm)
    maxPosition = a.index(maxm)
    index.append(str(maxPosition))
    a[maxPosition] = a[n-1]
    a[n-1] = maxm
    a.pop(n-1)
    n -= 1
    

#print(' '.join(index))