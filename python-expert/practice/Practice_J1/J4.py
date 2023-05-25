from collections import Counter

numbers = []
for i in range(10):
    number = int(input(f""))
    numbers.append(number)

count = Counter(numbers)
max_count = max(count.values())
most_duplicated = [number for number, freq in count.items() if freq == max_count]

if len(most_duplicated) == 1:
    print(f"{most_duplicated[0]}\n{max_count}")
else:
    print(f"{max_count}{most_duplicated}")
