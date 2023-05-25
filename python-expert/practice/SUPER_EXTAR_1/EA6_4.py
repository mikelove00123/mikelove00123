import sys

n=int(input(""))
a=1
while a<=n:
    b = 1
    while b <= n*2-1:
        if (b==n+1-a or 
            b==a+n-1 or 
            b== 3*n-a-1 or 
            b==a-n+1):
            sys.stdout.write("x")
        else:
            sys.stdout.write("-")
        b =b+1
    print()
    a=a+1

