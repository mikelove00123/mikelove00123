x=[]
for i in range(0,10):
    x.append(int(input()))
v=int(input())
index=int(input())

x.insert(index, v)
del x[len(x)-1]
print(x)