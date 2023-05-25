import sys

n=5
a=1
while a<=n*2-1:
    b = 1
    while b <= n*2-1:
        if b==a or b==2*n-a:
            sys.stdout.write("x")
        else:
            sys.stdout.write("-")
        b =b+1
    print()
    a=a+1
