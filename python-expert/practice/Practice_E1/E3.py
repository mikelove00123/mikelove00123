k = int(input(""))
l = int(input(""))
a, b = k, l
while b:
    a, b = b, a % b
gcd = a
lcm = (k * l) // gcd
print(lcm)
