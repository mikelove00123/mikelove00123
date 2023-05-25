x = []
for i in range(0,10):
    n = int(input(""))
    x.append(n)
    
i = 0
while i < len(x):
    if x[i] % 2 == 0:
        print(x[i])
    i += 1
