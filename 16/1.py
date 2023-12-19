import numpy as np
from enum import Enum
import sys


with open("16/test.txt") as f:
    map = f.readlines()

map = [row.strip() for row in map]

# print(map)

energized = np.zeros((len(map), len(map[0])))


Entrypoint = Enum("Entrypoint", ["N", "S", "W", "E"])

entrypoints = set()


def beam(x, y, entrypoint):
    if x < 0 or y < 0 or x >= len(map[0]) or y >= len(map):
        return

    while not (x < 0 or y < 0 or x >= len(map[0]) or y >= len(map)):
        if (x, y, entrypoint) in entrypoints:
            return
        else:
            entrypoints.add((x, y, entrypoint))

        energized[y][x] = True
        tile = map[y][x]
        print(x,y)
        if tile == "-" and entrypoint in [Entrypoint.N, Entrypoint.S]:
            beam(x + 1, y, Entrypoint.W)
            beam(x - 1, y, Entrypoint.E)
            return
        if tile == "|" and entrypoint in [Entrypoint.W, Entrypoint.E]:
            beam(x, y - 1, Entrypoint.S)
            beam(x, y + 1, Entrypoint.N)
            return

        if entrypoint == Entrypoint.N:
            if tile == "." or tile == "|":
                y += 1
            if tile == "\\":
                x += 1
                entrypoint = Entrypoint.W
            if tile == "/":
                x -= 1
                entrypoint = Entrypoint.E
        elif entrypoint == Entrypoint.S:
            if tile == "." or tile == "|":
                y -= 1
            if tile == "\\" or tile == "-":
                x -= 1
                entrypoint = Entrypoint.E
            if tile == "/" or tile == "-":
                x += 1
                entrypoint = Entrypoint.W
        elif entrypoint == Entrypoint.W:
            if tile == "." or tile == "-":
                x += 1
            if tile == "\\" or tile == "|":
                y+=1
                entrypoint = Entrypoint.N
            if tile == "/" or tile == "|":
                y-=1
                entrypoint = Entrypoint.S
        elif entrypoint == Entrypoint.E:
            if tile == "." or tile == "-":
                x -= 1
            if tile == "\\" or tile == "|":
                y-=1
                entrypoint = Entrypoint.S
            if tile == "/" or tile == "|":
                y+=1
                entrypoint = Entrypoint.N


beam(0, 0, Entrypoint.W)
# print(energized)
print(energized.sum())
