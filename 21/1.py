import numpy as np

with open("21/input.txt") as f:
    data = f.readlines()

map = np.zeros((len(data), len(data[0].strip())), dtype=int)
state = np.zeros_like(map)

for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c == ".":
            map[y][x] = 1
        elif c == "S":
            map[y][x] = 1
            state[y][x] = 1

for i in range(64):
    new_state = np.zeros_like(map)
    for y, row in enumerate(state):
        for x, col in enumerate(row):
            if col:
                if y > 0:
                    ind = (y - 1, x)
                    new_state[ind] = map[ind]
                if y < map.shape[0] - 1:
                    ind = (y + 1, x)
                    new_state[ind] = map[ind]
                if x > 0:
                    ind = (y, x - 1)
                    new_state[ind] = map[ind]
                if x < map.shape[1] - 1:
                    ind = (y, x + 1)
                    new_state[ind] = map[ind]
    state = new_state
print(state.sum())
