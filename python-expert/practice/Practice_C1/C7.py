import sys

b = 1
while b < 11:
    a = 0
    while a <= 9 - b:
        sys.stdout.write("-")
        a = a + 1
    x = 1
    while x <= b:
        sys.stdout.write(str(x))
        x=x+1
    x = 1
    while x <= b-1:
        sys.stdout.write(str(b-x))
        x=x+1
    print()
    b=b+1
