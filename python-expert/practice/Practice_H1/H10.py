x=[]
for i in range(0,10):
    n = int(input(""))
    x.append(n)
min= x[0]
for y in x:
    if min > y:
        min=y
print(min)