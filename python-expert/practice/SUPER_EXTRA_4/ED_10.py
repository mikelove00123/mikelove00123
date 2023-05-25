#08_python_Day_7
#python7_7
hrs=[]
for i in range(0,5):
    hrs.append([])
    for j in range(0,7):
        hrs[i].append(int(input()))
for i in range(0,5):
    for j in range(0,7):
        continue
        print(hrs[i][j],"\t",end=" ")
    print()
sum=[]
for i in range(0,5):
    sum.append(0)
    for j in range(0,7):
        sum[i]=sum[i]+hrs[i][j]
        
print(sum)

