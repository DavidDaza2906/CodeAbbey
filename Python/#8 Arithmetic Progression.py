
c = []
n= int(input())
for x in range(n):
    x = input().split()
    firstValue = int(x[0])
    steps = int(x[1])
    times = int(x[2])
    contador = 1
    finalValue = 0
    while contador <= times:
        contador +=1 
        finalValue += firstValue
        firstValue += steps
        print(finalValue)
    c.append(str(finalValue))
print(' '.join(c))
