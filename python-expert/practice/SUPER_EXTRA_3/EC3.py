x=[]
for i in range(0,10):
    x.append(int(input()))

Max=x[0]
maxindex=0
i=0

for i in range(len(x)):
    if x[i]>Max:
        Max=x[i]
        maxindex=i
    i=i+1
print(Max)
print(maxindex)