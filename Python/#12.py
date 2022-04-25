from distutils.cygwinccompiler import Mingw32CCompiler
from locale import DAY_2

import math
def timeDifference(day1,hour1,min1,sec1,day2,hour2,min2,sec2):
    dayF = day2 - day1 
    hourF = round((hour2-hour1)-0.5)
    hourF = hourF%60
    minF = min2 - min1
    secF = sec2- sec1
    return dayF, hourF, minF,secF

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
    print(timeDifference(day1,hour1,min1,sec1,day2,hour2,min2,sec2))