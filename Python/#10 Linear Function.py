def linearFunction(x1,y1,x2,y2):
    return int((y2-y1)/(x2-x1))
def function(a):
    return int(-((a*x2)-y2))    
k = []
n = int(input())
for _ in range(n):
    u = input().split()
    for x in u:
        x1 = int(u[0])
        y1 = int(u[1])
        x2 = int(u[2])
        y2 = int(u[3])
    a = linearFunction(x1,y1,x2,y2)
    b = function(a)
    k.append('({0} {1})'.format(a,b))
print(' '.join(k))