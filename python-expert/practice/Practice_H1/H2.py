x=[]
for i in range(0,10):
    n = int(input(""))
    x.append(n)
i=len(x)-1
x.reverse()
for i in reversed(range(0,len(x))):
    print(x[i])