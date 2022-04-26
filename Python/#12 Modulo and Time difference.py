
import math
def timeDifference(day1,hour1,min1,sec1,day2,hour2,min2,sec2):
    if sec2 >= sec1:
        s = sec2-sec1
    else: 
        min2 -=1
        sec2 +=60
        s = sec2 -sec1
    if min2 >= min1:
        m = min2-min1
    else:
        hour2 -=1
        min2 += 60
        m = min2-min1
    if hour2 >= hour1:
        h = hour2-hour1

    else:
        day2 -=1
        hour2+= 24
        h= hour2-hour1
    d = day2-day1
    k.append('('+str(d)+' '+ str(h)+' '+str(m)+' '+str(s)+')')
k = []
n = int(input())
for _ in range(n):
    a = input().split()
    day1 = int(a[0])
    hour1 = int(a[1])
    min1 = int(a[2])
    sec1 = int(a[3])
    day2 = int(a[4])
    hour2 = int(a[5])
    min2 = int(a[6])
    sec2 = int(a[7])
    timeDifference(day1,hour1,min1,sec1,day2,hour2,min2,sec2)
print(' '.join(k))