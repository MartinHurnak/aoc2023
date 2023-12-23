import numpy as np

with open("23/input.txt") as f:
    data = f.readlines()

map = [row.strip() for row in data]
visited = np.zeros((len(map), len(map[0])))

# Use dfs to search all possible paths, remeber the lenght of longest one

stack = []
maxdepth = 0


def unvisit(y, x):
    visited[y][x] = False


def dfs(y, x, depth=0):
    global maxdepth
    if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
        return
    if map[y][x] == "#" or visited[y][x]:
        return

    # finish
    if x == len(map[0]) - 2 and y == len(map) - 1:
        maxdepth = max(depth, maxdepth)

    visited[y][x] = True
    stack.append(lambda: unvisit(y, x))
    if map[y][x] == "^":
        stack.append(lambda: dfs(y - 1, x, depth + 1))
    elif map[y][x] == "v":
        stack.append(lambda: dfs(y + 1, x, depth + 1))
    elif map[y][x] == ">":
        stack.append(lambda: dfs(y, x + 1, depth + 1))
    elif map[y][x] == "<":
        stack.append(lambda: dfs(y, x - 1, depth + 1))
    elif map[y][x] == ".":
        stack.append(lambda: dfs(y - 1, x, depth + 1))
        stack.append(lambda: dfs(y + 1, x, depth + 1))
        stack.append(lambda: dfs(y, x + 1, depth + 1))
        stack.append(lambda: dfs(y, x - 1, depth + 1))
    return


dfs(0, 1)
while stack:
    stack.pop()()
print(maxdepth)
