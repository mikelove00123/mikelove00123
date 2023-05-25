a=50e6
b=70e6

year =1

while True:
    a=a*(103/100)
    b=b*(102/100)
    if a>b:
        break
    year+=1    
print(year)


#สูตรย่อแบบimport
"""
import math
n=math.log(5/7,1023/1.23)
prit(n)
"""