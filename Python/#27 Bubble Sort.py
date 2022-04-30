n = int(input())
a = input().split()
a = [int(x) for x in a]
swap = 0
paso = 0
r = False
while not r:
    r = True
    paso +=1
    for i in range(n-1):
        if not a[i]  <= a[i+1]:
            r = False
            t = a[i]
            a[i] = a[i+1]
            a[i+1] = t
            swap +=1
            
    

print(paso,swap)

