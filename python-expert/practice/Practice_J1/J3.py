numbers = []
for i in range(10):
    number = float(input(f""))
    numbers.append(number)
numbers.sort()
if len(numbers) % 2 == 0:
    middle_index_1 = len(numbers) // 2 - 1
    middle_index_2 = len(numbers) // 2
    median = (numbers[middle_index_1] + numbers[middle_index_2]) / 2
else:
    middle_index = len(numbers) // 2
    median = numbers[middle_index]

print(f"{median}")
