import re


with open("2/input.txt") as f:
    games = f.readlines()


sum = 0
for game in games:
    power = 1
    for color in ["red", "green", "blue"]:
        cube_counts = [int(i) for i in re.findall(f"[0-9]+(?= {color})", game)]
        power *= max(cube_counts)
    sum += power
print(sum)
