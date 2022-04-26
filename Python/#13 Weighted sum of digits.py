
import math
n = input()
k = []
total = input().split()
for number in total:
    counter = 0
    digitsTotal = []
    number = int(number)
    wds = 0
    while number > 0:
        digit = math.floor(number%10)
        number = math.floor(number/10)
        digitsTotal.append(digit)
    digitsTotal.reverse()
    for x in digitsTotal:
        counter += 1
        s = x* counter
        wds += s
    k.append(str(wds))
print(' '.join(k))

