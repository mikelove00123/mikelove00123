import math
n = int(input(""))
sum = 0
a = 1
while a<=n:
    sum += 1/a**2
    a=a+1
print (math.sqrt (6*sum))