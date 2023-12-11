import re

with open("1/input.txt") as f:
    data = f.readlines()

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

sum = 0
for line in data:
    matches =re.findall(f"(?=({'|'.join(['[0-9]', *digits.keys()])}))" , line, flags=0)    
    first = digits.get(matches[0], matches[0])
    last = digits.get(matches[-1], matches[-1])
    sum += int(first + last)
    print(line, matches, first, last, sum)
print(sum)
