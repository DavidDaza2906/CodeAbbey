
from re import A


def gcd(a,b):
    while True:
        b = b%a
        if b == 0:
            return a
            break
        a = a%b
        if a == 0:
            return b
            break
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