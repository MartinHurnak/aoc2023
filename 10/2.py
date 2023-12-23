from collections import deque
import numpy as np

with open("10/input.txt") as f:
    map = f.readlines()

map = np.array([list(row.strip()) for row in map])
visited = np.zeros_like(map, dtype=int)
start = (
    np.where(map == "S")[0][0],
    np.where(map == "S")[1][0],
)
stack = deque()


def go(map, y, x):
    tile = map[y, x]
    visited[y, x] = True
    north, south, west, east = False, False, False, False
    if tile == "F":
        south, east = True, True
    elif tile == "L":
        north, east = True, True
    elif tile == "7":
        south, west = True, True
    elif tile == "J":
        north, west = True, True
    elif tile == "|":
        north, south = True, True
    elif tile == "-":
        east, west = True, True
    elif tile == "S":
        if y > 0 and map[y - 1, x] in ["|", "F", "7"]:
            north = True
        if y < len(map) - 1 and map[y + 1, x] in ["|", "L", "J"]:
            south = True
        if x > 0 and map[y, x - 1] in ["-", "F", "L"]:
            west = True
        if x < len(map[y]) - 1 and map[y, x + 1] in ["-", "7", "J"]:
            east = True
        if north and south:
            map[y, x] = "|"
        elif north and east:
            map[y, x] = "L"
        elif north and west:
            map[y, x] = "J"
        elif south and east:
            map[y, x] = "F"
        elif south and west:
            map[y, x] = "7"
        elif west and east:
            map[y, x] = "-"

    if north and not visited[y - 1, x]:
        visited[y - 1, x] = True
        stack.append(lambda: go(map, y - 1, x))

    if south and not visited[y + 1, x]:
        visited[y + 1, x] = True
        stack.append(lambda: go(map, y + 1, x))

    if west and not visited[y, x - 1]:
        visited[y, x - 1] = True
        stack.append(lambda: go(map, y, x - 1))

    if east and not visited[y, x + 1]:
        visited[y, x + 1] = True
        stack.append(lambda: go(map, y, x + 1))


# find the main loop
go(map, *start)
while stack:
    stack.popleft()()

# remove all the pipes that are not the part of the main loop
map[visited != 1] = "."

# out of each "." shoot ray to the west. if it goes through odd number of edges, tile is inside
# if it goes through even number of edges, tile is outside
# bends will be bypassed from the south side, so we can pass around J and L but F and 7 are considered as edges
inside = 0
for y, row in enumerate(map):
    for x, tile in enumerate(row):
        if tile == ".":
            if np.sum(np.isin(map[y, 0:x], ("F", "7", "|"))) % 2 == 1:
                inside += 1


print(inside)
