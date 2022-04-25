def bmi(weight,height):
    BMI = weight/(height**2)
    if BMI < 25.0:
        if BMI < 18.5:
            return 'under'
        else:
            return 'normal'
    else:
        if BMI < 30.0:
            return 'over'
        else:
            return 'obese'
        
n = int(input())
k = []
for x in range(n):
    l = input().split()
    weight = int(l[0])
    height = float(l[1])
    k.append(bmi(weight,height))
print(' '.join(k))