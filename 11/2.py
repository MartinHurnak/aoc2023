import numpy as np

with open("11/input.txt") as f:
    map_txt = f.readlines()

EXPAND_RATE = 1000000 - 1
map = np.zeros((len(map_txt), len(map_txt[0].strip())))

for i, row in enumerate(map_txt):
    for j, c in enumerate(row.strip()):
        if c == "#":
            map[i][j] = 1

galaxies = np.argwhere(map)
empty_cols = np.where(~map.any(axis=0))[0]
empty_rows = np.where(~map.any(axis=1))[0]


total = 0

for i in range(len(galaxies)):
    galaxies[i][0] += EXPAND_RATE * np.sum(empty_rows < galaxies[i][0])
    galaxies[i][1] += EXPAND_RATE * np.sum(empty_cols < galaxies[i][1])


for i, galaxy in enumerate(galaxies):
    for galaxy2 in galaxies[i:]:
        total += np.sum(np.abs(galaxy2 - galaxy))

print(total)
