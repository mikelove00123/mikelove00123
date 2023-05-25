x=[]
for i in range(0,10):
    x.append(int(input()))
v=int(input())
index=-1
for i in range(0,len(x)):
    if x[i]==v:
        index=i
        break
if index==-1:
    print("not")
else:    
    x.pop(index)
    x.append(0)
print(x)