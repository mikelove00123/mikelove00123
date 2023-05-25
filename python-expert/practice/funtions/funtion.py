def mypower(a,n):
    p=1
    for i in range(0,n):
        p*=a
    return p

def myfac(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p

def sin(x):
    sumx=0
    for i in range(1,100,2):
        if i %4==1:
            sumx+=mypower(x,i)/myfac(i)
        else:
            sumx-=mypower(x,i)/myfac(i)
        print(i,sumx)
    return sumx
import math    
print(sin(math.pi/2))