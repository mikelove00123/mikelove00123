last_sum=0
sum=0
i=1
while True:
    if i%4==1:
        sum=sum+4*1/i
    else :
        sum=sum-4*1/i
    if abs(sum-last_sum)<0.0001:
        break
    last_sum=sum
    i=i+2
print(sum)
