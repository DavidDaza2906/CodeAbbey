n = int(input())
a = input().split()
result = 0
for x in a:
    result += int(x)
    result *= 113
result %= 10000007
print(result)