n = int(input())
k = []
for _ in range(n):
    numbers= float(input())
    dice = int(numbers*6)+1
    k.append(str(dice))
print(' '.join(k))