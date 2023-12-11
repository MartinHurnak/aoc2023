import re
with open("3/input.txt") as f:
    plan = f.readlines()

symbols = []
for row in plan:
    symbols_row = []
    for i,c in enumerate(row.strip()):
        if c != "." and not c.isdigit():
            symbols_row.append(i)
    symbols.append(symbols_row)

def has_adjacent_symbol(number, row_index):
    for adjacent_row in symbols[max(row_index-1, 0):row_index+2]:
        for symbol in adjacent_row:
            if symbol >= number.start(0) - 1 and symbol <=  number.end(0):
                return True
    return False

sum = 0
for i, row in enumerate(plan):
    numbers =list(re.finditer(r"[0-9]+", row))
    for number in numbers:
        if has_adjacent_symbol(number, i):
            sum += int (number.group(0))
         
print(sum)
