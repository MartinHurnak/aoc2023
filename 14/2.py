import numpy as np

with open("14/input.txt") as f:
    platform = f.readlines()

platform = [row.strip() for row in platform]


fixed_rocks_cols = [[] for _ in range(len(platform[0]))]
fixed_rocks_rows = [[] for _ in range(len(platform))]
rolling_rocks = []


for row_index, row in enumerate(platform):
    for col_index, c in enumerate(row):
        if c == "#":
            fixed_rocks_rows[row_index].append(col_index)
            fixed_rocks_cols[col_index].append(row_index)
        elif c == "O":
            rolling_rocks.append((row_index, col_index))

fixed_rocks_cols = [np.array(l) for l in fixed_rocks_cols]
fixed_rocks_rows = [np.array(l) for l in fixed_rocks_rows]


def next_fixed_in(fixed_rocks, index, reverse=False):
    if reverse:
        return int(fixed_rocks[fixed_rocks > index].min(initial=len(platform)) - 1)
    return int(fixed_rocks[fixed_rocks < index].max(initial=-1) + 1)


def roll_north():
    rolling_rocks.sort(key=lambda x: (x[1], x[0]))
    index_free = 0
    col_index = 0
    for i, rock in enumerate(rolling_rocks):
        if rock[1] != col_index:
            index_free = 0
            col_index = rock[1]

        index_free = max(
            index_free, next_fixed_in(fixed_rocks_cols[col_index], rock[0])
        )

        rolling_rocks[i] = (index_free, rock[1])
        index_free += 1


def roll_south():
    rolling_rocks.sort(key=lambda x: (x[1], x[0]), reverse=True)
    index_free = len(platform) - 1
    col_index = 0
    for i, rock in enumerate(rolling_rocks):
        if rock[1] != col_index:
            index_free = len(platform) - 1
            col_index = rock[1]
        index_free = min(
            index_free,
            next_fixed_in(fixed_rocks_cols[col_index], rock[0], reverse=True),
        )

        rolling_rocks[i] = (index_free, rock[1])
        index_free -= 1


def roll_west():
    rolling_rocks.sort(key=lambda x: (x[0], x[1]))
    index_free = 0
    row_index = 0
    for i, rock in enumerate(rolling_rocks):
        if rock[0] != row_index:
            index_free = 0
            row_index = rock[0]
        index_free = max(
            index_free, next_fixed_in(fixed_rocks_rows[row_index], rock[1])
        )
        rolling_rocks[i] = (rock[0], index_free)
        index_free += 1


def roll_east():
    rolling_rocks.sort(key=lambda x: (x[0], x[1]), reverse=True)
    index_free = 0
    row_index = 0
    for i, rock in enumerate(rolling_rocks):
        if rock[0] != row_index:
            index_free = len(platform)
            row_index = rock[0]
        index_free = min(
            index_free,
            next_fixed_in(fixed_rocks_rows[row_index], rock[1], reverse=True),
        )
        rolling_rocks[i] = (rock[0], index_free)
        index_free -= 1


def spin_cycle():
    before = set(rolling_rocks)
    roll_north()
    roll_west()
    roll_south()
    roll_east()
    if set(rolling_rocks) == before:
        raise StopIteration


def print_platform():
    newplatform = [["." for _ in range(len(platform[0]))] for _ in range(len(platform))]
    for row_index, col in enumerate(fixed_rocks_rows):
        for col_index in col:
            newplatform[row_index][col_index] = "#"

    # print(rolling_rocks)
    for rock in rolling_rocks:
        newplatform[int(rock[0])][int(rock[1])] = "O"

    for row in newplatform:
        print("".join(row))


states = set()
states_index = {}
cycle_loop = None
CYCLES = 1000000000
i = 0
while i < CYCLES:
    if cycle_loop is None:
        states.add(frozenset(rolling_rocks))
        states_index[frozenset(rolling_rocks)] = i
    spin_cycle()
    i += 1
    if cycle_loop is None and set(rolling_rocks) in states:
        cycle_loop = i - states_index[frozenset(rolling_rocks)]
        i += int((CYCLES - i) / cycle_loop) * cycle_loop
        print(f"Moving by {cycle_loop} steps to {i}")


print_platform()
total_load = 0
maxload = len(platform)
for rock in rolling_rocks:
    total_load += maxload - (rock[0])

print(total_load)
