w1 = float(input())
p1 = float(input())

w2 = float(input())
p2 = float(input())

ppw1 = p1 / w1
ppw2 = p2 / w2

if ppw1 < ppw2:
    print("A is cheaper than B")
elif ppw2 < ppw1:
    print("B is cheaper than A")
else:
    print("Equal price")
