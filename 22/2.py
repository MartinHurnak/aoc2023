import numpy as np
import copy

with open("22/input.txt") as f:
    data = f.readlines()


class Point:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


class Block:
    def __init__(self, block_index, line_string) -> None:
        self.index = block_index
        start, end = line_string.strip().split("~")
        self.start = Point(*[int(i) for i in start.split(",")])
        self.start = Point(*[int(i) for i in start.split(",")])
        self.end = Point(*[int(i) for i in end.split(",")])
        self.start.z -= 1
        self.end.z -= 1


blocks = [Block(i + 1, l) for i, l in enumerate(data)]
blocks.sort(key=lambda l: l.start.z)
x_max = max([b.start.x for b in blocks] + [b.end.x for b in blocks])
y_max = max([b.start.y for b in blocks] + [b.end.y for b in blocks])
z_max = max([b.start.z for b in blocks] + [b.end.z for b in blocks])

print(x_max, y_max, z_max)

map = np.zeros((z_max + 1, y_max + 1, x_max + 1))

# insert blocks into map
for block in blocks:
    map[
        block.start.z : block.end.z + 1,
        block.start.y : block.end.y + 1,
        block.start.x : block.end.x + 1,
    ] = block.index

# block falling
block_moved = True
while block_moved:
    block_moved = False
    for block in blocks:
        # remove block from map
        map[
            block.start.z : block.end.z + 1,
            block.start.y : block.end.y + 1,
            block.start.x : block.end.x + 1,
        ] = 0
        # move block down until it collides with block below
        while (
            block.start.z > 0
            and block.end.z > 0
            and map[
                block.start.z - 1 : block.end.z,
                block.start.y : block.end.y + 1,
                block.start.x : block.end.x + 1,
            ].sum()
            == 0
        ):
            block.start.z -= 1
            block.end.z -= 1
            block_moved = True
        # insert block into new position
        map[
            block.start.z : block.end.z + 1,
            block.start.y : block.end.y + 1,
            block.start.x : block.end.x + 1,
        ] = block.index

# get supporting blocks
block_supported_by = {}
for block in blocks:
    # get overlapping blocks on z+1 (blocks supported by this block)
    supporting = np.unique(
        map[
            block.end.z + 1,
            block.start.y : block.end.y + 1,
            block.start.x : block.end.x + 1,
        ]
    )
    for b in supporting[supporting != 0]:
        block_supported_by.setdefault(int(b), []).append(block.index)


def remove(state: dict, supporting_block: int):
    fallen = 1
    for block in state.keys():
        if supporting_block in state[block]:
            state[block].remove(supporting_block)
            if state[block] == []:
                fallen += remove(state, block)  # chain-reaction
    return fallen


fallen = 0
for block in blocks:
    state = copy.deepcopy(block_supported_by)
    # -1 because first block was disintegrated (it did not fall)
    fallen += remove(state, block.index) - 1

print(fallen)
