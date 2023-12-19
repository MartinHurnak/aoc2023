with open("15/input.txt") as f:
    data = f.read()

sequences = data.strip("\n").split(",")

result = 0
for seq in sequences:
    hash = 0
    for c in seq:
        hash = ((hash + ord(c)) * 17) % 256
    result += hash

print(result)
