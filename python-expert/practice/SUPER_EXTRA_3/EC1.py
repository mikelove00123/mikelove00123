x=[]
for i in range(0,10):
    x.append(int(input()))
num=0
for i in range(0,10):
    if  x[i]>=10:
        num+=1
print(num)
