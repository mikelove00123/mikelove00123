import random
import time
x=[]
x=[1,2,3]
random.seed()
for i in range(0,5000):
    x.append(random.randrange(10000))

start=time.time()
for j in range(0,len(x)):
    for i in range(0,len(x)-1-j):
        if x[i]>x[i+1]:
            t=x[i]
            x[i]=x[i+1]
            x[i+1]=t
end=time.time()
uset1=end-start
print(uset1)

