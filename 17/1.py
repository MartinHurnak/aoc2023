import numpy as np
from enum import IntEnum

with open("17/test.txt") as f:
    data = f.readlines()

data = [row.strip() for row in data]

map = np.zeros((len(data), len(data[0])))
for i, row in enumerate(data):
    for j, digit in enumerate(row):
        map[i][j] = int(digit)


class Direction(IntEnum):
    N = 0
    W = 1
    S = 2
    E = 3


def score_neighbours(skip_direction, x, y):
    north, west, south, east = 0, 0, 0, 0
    origin = (skip_direction, x, y)
    for i in range(3):
        if skip_direction not in [Direction.S, Direction.N]:
            if x > i:
                ind = (Direction.N, x - 1 - i, y)
                north += map[x - 1 - i, y]
                if not visited[ind]:
                    if total_dist[origin] + north < total_dist[ind]:
                        total_dist[ind] = total_dist[origin] + north
                        prev[ind] = origin
            if x < map.shape[0] - 1 - i:
                ind = (Direction.S, x + 1 + i, y)
                south += map[x + 1 + i, y]
                if not visited[ind]:
                    if total_dist[origin] + south < total_dist[ind]:
                        total_dist[ind] = total_dist[origin] + south
                        prev[ind] = origin
        if skip_direction not in [Direction.W, Direction.E]:
            if y > i:
                ind = (Direction.W, x, y - 1 - i)
                west += map[x, y - 1 - i]
                if not visited[ind]:
                    if total_dist[origin] + west < total_dist[ind]:
                        total_dist[ind] = total_dist[origin] + west
                        prev[ind] = origin
            if y < map.shape[1] - 1 - i:
                ind = (Direction.E, x, y + 1 + i)
                east += map[x, y + 1 + i]
                if not visited[ind]:
                    if total_dist[origin] + east < total_dist[ind]:
                        total_dist[ind] = total_dist[origin] + east
                        prev[ind] = origin


visited = np.array([np.zeros_like(map, dtype=bool)] * 4)
total_dist = np.full_like(visited, np.inf, dtype=np.number)
prev = np.empty_like(total_dist, dtype=tuple)

total_dist[:, 0, 0] = 0
visited[:, 0, 0] = True
for direction in [Direction.N, Direction.E, Direction.S, Direction.W]:
    score_neighbours(direction, 0, 0)

while not (visited[Direction.E, -1, -1] and visited[Direction.S, -1, -1]):
    index = np.unravel_index(
        np.where(~visited, total_dist, np.inf).argmin(), total_dist.shape
    )  # priority queue would be faster, this is lazy

    if visited[index]:
        print(total_dist)
        raise Exception

    visited[index] = True
    score_neighbours(*index)
print(total_dist[:, -1, -1].min())
