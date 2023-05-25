a=[]
for i in range(0,10):
    a.append(int(input()))
b=[]
for i in range(0,10):
    b.append(int(input()))
c=[]

for i in range(0,1):
    c.extend(a)
    c.extend(b)
print(c)