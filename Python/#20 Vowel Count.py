n = int(input())
b = []
for x in range(n):
    vocales = 0
    a = input()
    for i in a:
        if i in ('aeiouy'):
            vocales += 1
    b.append(str(vocales))
print(' '.join(b))