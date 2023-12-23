import numpy as np

with open("23/input.txt") as f:
    data = f.readlines()

map = [row.strip() for row in data]
visited = np.zeros((len(map), len(map[0])))


# Use dfs to search all possible paths, remeber the lenght of longest one
# Optimize previous solution by searching just for crossroads and paths between them, and "jump" between crossroads
# still slow, but gets the job done


def is_crossroad(y, x):
    if map[y][x] == "#":
        return False
    paths = 0
    if y > 0 and map[y - 1][x] != "#":
        paths += 1
    if y < len(map) - 1 and map[y + 1][x] != "#":
        paths += 1
    if x > 0 and map[y][x - 1] != "#":
        paths += 1
    if x < len(map[0]) - 1 and map[y][x + 1] != "#":
        paths += 1
    return paths > 2


paths = {}
finish = (len(map) - 1, len(map[0]) - 2)


def dfs_path_search(origin, y, x, steps=0):
    if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
        return
    if map[y][x] == "#" or visited[y][x]:
        return

    # finish
    if (y, x) == finish:
        paths.setdefault(origin, []).append((y, x, steps))
        return

    if is_crossroad(y, x) and (y, x) != origin:
        paths.setdefault(origin, []).append((y, x, steps))
        return

    visited[y][x] = True
    dfs_path_search(origin, y - 1, x, steps + 1)
    dfs_path_search(origin, y + 1, x, steps + 1)
    dfs_path_search(origin, y, x + 1, steps + 1)
    dfs_path_search(origin, y, x - 1, steps + 1)
    visited[y][x] = False
    return


# search nearest crossroad from start
dfs_path_search((0, 1), 0, 1)
# search all paths between regular crossroads
for y, row in enumerate(map):
    for x, tile in enumerate(row):
        if not is_crossroad(y, x):
            continue
        dfs_path_search((y, x), y, x)


visited_crossroads = set()


def dfs(point: tuple, steps=0):
    if point == finish:
        return steps

    visited_crossroads.add(point)
    maxsteps = 0
    for path in paths[point]:
        if path[0:2] not in visited_crossroads:
            maxsteps = max(dfs(path[0:2], path[2] + steps), maxsteps)
    visited_crossroads.remove(point)
    return maxsteps


print(dfs((0, 1)))
