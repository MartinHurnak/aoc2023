from collections import deque

with open("10/input.txt") as f:
    map = f.readlines()

visited = []
length = []
for row in map:
    visited.append([False] * len(row))
    length.append([0] * len(row))

for i in range(len(map)):
    j = map[i].find("S")
    if j != -1:
        break

# print(map)
# print(map[i][j])

stack = deque()


def go(map, x, y, d=-1):
    tile = map[x][y]
    visited[x][y] = True
    length[x][y] = d + 1
    # print(x, y, d+1)
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
        if x > 0 and map[x - 1][y] in ["|", "F", "7"]:
            north = True
        if x < len(map) - 1 and map[x + 1][y] in ["|", "L", "J"]:
            south = True
        if y > 0 and map[x][y - 1] in ["-", "F", "L"]:
            west = True
        if y < len(map[x]) - 1 and map[x][y + 1] in ["-", "7", "J"]:
            east = True

    if north and not visited[x - 1][y]:
        visited[x - 1][y] = True
        # print("GO", x-1, y, d+2)
        stack.append(lambda: go(map, x - 1, y, d + 1))

    if south and not visited[x + 1][y]:
        visited[x + 1][y] = True
        # print("GO", x+1, y, d+2)
        stack.append(lambda: go(map, x + 1, y, d + 1))

    if west and not visited[x][y - 1]:
        visited[x][y - 1] = True
        # print("GO", x, y-1, d+2)
        stack.append(lambda: go(map, x, y - 1, d + 1))

    if east and not visited[x][y + 1]:
        visited[x][y + 1] = True
        # print("GO", x, y+1, d+2)
        stack.append(lambda: go(map, x, y + 1, d + 1))
    return d + 1


go(map, i, j)
max = 0
while stack:
    tmp = stack.popleft()()
    if tmp > max:
        max = tmp

print(max)
