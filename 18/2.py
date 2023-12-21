with open("18/input.txt") as f:
    data = f.readlines()

surface = 0
current = (0, 0)  # (y, x)
for line in data:
    prev = current
    _, _, hex = line.strip().split()
    hex = hex.strip("()").strip("#")
    length = int(hex[:-1], 16)
    direction = ["R", "D", "L", "U"][int(hex[-1])]
    if direction == "R":
        current = (current[0], current[1] + length)
    elif direction == "L":
        current = (current[0], current[1] - length)
    elif direction == "U":
        current = (current[0] - length, current[1])
    elif direction == "D":
        current = (current[0] + length, current[1])
    surface += (current[0] * prev[1] - current[1] * prev[0]) / 2  # shoelace formula
    surface += (
        abs(current[0] - prev[0]) + abs(current[1] - prev[1])
    ) / 2  # formula counts only inside - add wall as well

surface += 1  # initial-position
print(surface)
