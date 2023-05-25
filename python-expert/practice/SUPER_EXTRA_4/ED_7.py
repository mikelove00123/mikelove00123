#08_python_Day_7
#python7_6
def isPrime(n):
    count=0
    i=1
    while i<=n:
        if n%i==0:
            count=count+1
        i=i+1
    if count==2:
        return 1
    else:
        return 0
n=int(input())
print(isPrime(n))
