age = input()
bmi = input()
young = age < 45
slim = bmi < 22.0

if young:
    if slim:v
        risk = 'low'
    else:
        risk = 'medium'
else:
    if slim:
        risk = 'medium'
    else:
        risk = 'high'