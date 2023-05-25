import sys

n=5
a=1
while a<=n:
    b = 1
    while b <= n-a:
        sys.stdout.write("-")
        b =b+1
    b = 1
    while b <= 2*a-1:
        sys.stdout.write("x")
        b=b+1
    print()
    a=a+1
