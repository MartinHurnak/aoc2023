import numpy as np
from enum import Enum

with open("16/input.txt") as f:
    map = f.readlines()

map = [row.strip() for row in map]

Entrypoint = Enum("Entrypoint", ["N", "S", "W", "E"])


def evaluate_energy(x, y, entrypoint):
    entrypoints = set()
    energized = np.zeros((len(map), len(map[0])))

    def beam(x, y, entrypoint, energized):
        if x < 0 or y < 0 or x >= len(map[0]) or y >= len(map):
            return

        while not (x < 0 or y < 0 or x >= len(map[0]) or y >= len(map)):
            if (x, y, entrypoint) in entrypoints:
                return
            else:
                entrypoints.add((x, y, entrypoint))

            energized[y][x] = True
            tile = map[y][x]
            # print(x,y)
            if tile == "-" and entrypoint in [Entrypoint.N, Entrypoint.S]:
                beam(x + 1, y, Entrypoint.W, energized)
                beam(x - 1, y, Entrypoint.E, energized)
                return
            if tile == "|" and entrypoint in [Entrypoint.W, Entrypoint.E]:
                beam(x, y - 1, Entrypoint.S, energized)
                beam(x, y + 1, Entrypoint.N, energized)
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
                    y += 1
                    entrypoint = Entrypoint.N
                if tile == "/" or tile == "|":
                    y -= 1
                    entrypoint = Entrypoint.S
            elif entrypoint == Entrypoint.E:
                if tile == "." or tile == "-":
                    x -= 1
                if tile == "\\" or tile == "|":
                    y -= 1
                    entrypoint = Entrypoint.S
                if tile == "/" or tile == "|":
                    y += 1
                    entrypoint = Entrypoint.N

    beam(x, y, entrypoint, energized)
    # print(energized)
    # print(energized.sum())
    return energized.sum()


best = 0
for i, _ in enumerate(map):
    best = max(best, evaluate_energy(0, i, Entrypoint.W))
    best = max(best, evaluate_energy(len(map) - 1, i, Entrypoint.E))

for i, _ in enumerate(map[0]):
    best = max(best, evaluate_energy(i, 0, Entrypoint.N))
    best = max(best, evaluate_energy(i, len(map[0]) - 1, Entrypoint.S))

print(best)
