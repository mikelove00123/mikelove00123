def mypower(a,n): #normal
    p=1
    for i in range(0,n):
        p*=a
    return p

def power(a,n): #loop/2
    x=1
    while n>0:
        if n%2==1:
            x=a*x
            n=n-1
        else:
            a=a*a
            n=n/2
    return x

def power2(a,n): #recursive
    if n==0:
        return 1
    if n==1:
        return a
    if n%2==1:
        return a*power2(a,n-1)
    t=power2(a,n/2)
    return t*t

import time
n=100000
millis =int(round(time.time()*1000))
power(2,n)
millis2 =int(round(time.time()*1000))
print("loop/2 : " , millis2-millis)

millis =int(round(time.time()*1000))
power2(2,n)
millis2 =int(round(time.time()*1000))
print("loop/2 recursive : " , millis2-millis)

millis =int(round(time.time()*1000))
mypower(2,n)
millis2 =int(round(time.time()*1000))
print("loop normal : " , millis2-millis)