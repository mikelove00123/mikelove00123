import sys

b = 0
while b < 10:
    a = 0
    while a <= b:
        sys.stdout.write("x")
        a = a + 1
    print()
    b = b + 1
