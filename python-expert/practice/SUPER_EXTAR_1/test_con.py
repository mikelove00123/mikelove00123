sum =0 
while True:
    n=int(input("n:"))
    if n==0:
        break
    if n%2==0:
        continue
    sum = sum+n
print(sum)    
