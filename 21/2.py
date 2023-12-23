import numpy as np
from collections import deque, defaultdict
import scipy

with open("21/input.txt") as f:
    data = f.readlines()

map = np.zeros((len(data), len(data[0].strip())), dtype=int)
start = None

for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c == ".":
            map[y, x] = 1
        elif c == "S":
            map[y, x] = 1
            start = (y, x)


def count_visited(map, start, limit):
    queue = deque()
    visited = set()
    distances = defaultdict(int)
    queue.append((start, 0))
    visited.add(start)
    while queue:
        point, d = queue.popleft()

        if d > limit:
            continue

        distances[d] += 1
        y, x = point
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if map[(y + dy) % map.shape[0], (x + dx) % map.shape[1]]:
                new_point = (y + dy, x + dx)
                if new_point not in visited:
                    visited.add(new_point)
                    queue.append((new_point, d + 1))

    return sum(list(distances.values())[limit % 2 :: 2])


size = map.shape[0]
steps = 26501365
# Lagrange interpolation
n = 3
y = [count_visited(map, start, size // 2 + i * size) for i in range(n)]
poly = scipy.interpolate.lagrange(range(n), y)
print(poly((steps - size // 2) // size))
