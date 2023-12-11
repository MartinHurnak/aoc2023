import re

with open("3/input.txt") as f:
    plan = f.readlines()


numbers = []
for i, row in enumerate(plan):
    numbers.append(list(re.finditer(r"[0-9]+", row)))


sum = 0
for i, row in enumerate(plan):
    for j, c in enumerate(row.strip()):
        if c == "*":
            adjacent_numbers = []
            for adjacent_row in numbers[max(i - 1, 0) : i + 2]:
                for number in adjacent_row:
                    if j >= number.start(0) - 1 and j <= number.end(0):
                        adjacent_numbers.append(number.group(0))
            if len(adjacent_numbers) == 2:
                sum += int(adjacent_numbers[0]) * int(adjacent_numbers[1])


print(sum)
