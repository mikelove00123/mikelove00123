x=[]
for i in range(0,10):
    n = int(input(""))
    x.append(n)
maxx= x[0]
for y in x:
    if maxx < y:
        maxx=y
print(maxx)