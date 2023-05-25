x = []
for i in range(0,10):
    n = int(input(""))
    x.append(n)
    
sum_of_numbers = sum(x)
average = sum_of_numbers / len(x)

print(average)
