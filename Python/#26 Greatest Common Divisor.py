def gcd(a,b):
    while True:
        c = b%a
        if c == 0:
            return a
            break
        d = a%c
        if d == a or d == 0:
            return 1
            break
        elif 
            return d
        
def lcm(a,b):
    d= int((a*b)/gcd(a,b))
    return d
k = []
n = int(input())
for _ in range(n):
    numbers = input().split()
    a = int(numbers[0])
    b = int(numbers[1])
    k.append('('+str(gcd(a,b)))
    k.append(str(lcm(a,b))+')')
print(' '.join(k))  