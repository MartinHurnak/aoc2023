import re


with open("2/input.txt") as f:
    games = f.readlines()


def validate_cube_count(game):
    color_limits = {"red": 12, "green": 13, "blue": 14}
    for color, limit in color_limits.items():
        cube_counts = re.findall(f"[0-9]+(?= {color})", game)
        for count in cube_counts:
            if int(count) > limit:
                return False
    return True

sum = 0
for game in games:
    if validate_cube_count(game):
        sum += int(re.search(r"(?<=Game )[0-9]*(?=:)", game).group(0))
print(sum)
