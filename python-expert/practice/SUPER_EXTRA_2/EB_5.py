import sys
n=int(input(""))
a=0
while a<=n:
    b=1
    while b<= n-a:
        sys.stdout.write("*")
        b+=1
    print()
    a+=1
