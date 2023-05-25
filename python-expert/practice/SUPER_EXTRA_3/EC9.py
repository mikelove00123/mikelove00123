import math
maxpower = int(input())
t=[]
while True:
    k=int(input())
    if k ==-999:
        break
    t.append(k)
s=[]
powercount=maxpower
for i in range(0,len(t)):
    if powercount !=-1:
        s.append((t[i])/(powercount+1))
    else:
        s.append(t[i])
    powercount = powercount-1
a=float(input())
b=float(input())
suma=0
sumb=0
pc=maxpower
for i in range(0,len(t)):
    if pc!=1:
        suma=suma+s[i]*pow(a, pc+1)
        sumb=sumb+s[i]*pow(b, pc+1)
    else:
        suma=suma+s[i]*math.log(a)
        sumb=sumb+s[i]*math.log(b)
    pc=pc-1
result=sumb-suma
print(result)

