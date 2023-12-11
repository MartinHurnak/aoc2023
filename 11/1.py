import numpy as np

with open("11/test.txt") as f:
    map_txt = f.readlines()

map = np.zeros((len(map_txt), len(map_txt[0].strip())))

for i, row in enumerate(map_txt):
    for j,c in enumerate(row.strip()):
        if c == "#":
            map[i][j] = 1

empty_cols = np.where(~map.any(axis=0))[0]
map = np.insert(map, empty_cols, 0, axis=1)
empty_rows = np.where(~map.any(axis=1))[0]
map = np.insert(map, empty_rows, 0, axis=0)
galaxies = np.argwhere(map)

total = 0
for i, galaxy in enumerate(galaxies):
    for galaxy2 in galaxies[i:]:
        total += np.sum(np.abs(galaxy2 - galaxy))

print(total)