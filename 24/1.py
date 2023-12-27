import numpy as np

with open("24/input.txt") as f:
    data = f.readlines()


class Hailstone:
    def __init__(self, hailstring):
        position, velocity = hailstring.strip().split(" @ ")
        self._position = np.array([int(i) for i in position.split(", ")])
        self._velocity = np.array([int(i) for i in velocity.split(", ")])

    @property
    def position(self):
        return self._position[:2]

    @property
    def velocity(self):
        return self._velocity[:2]

TESTAREA = 200000000000000, 400000000000000
# TESTAREA = 7, 27

hailstones = []
for line in data:
    hailstone = Hailstone(line)
    hailstones.append(hailstone)

collisions = 0
for i, hailstone in enumerate(hailstones):
    for other in hailstones[i:]:
        x, err, rank = np.linalg.lstsq(
            np.array([hailstone.velocity.T, -other.velocity.T]).T,
            other.position.T - hailstone.position.T,
        )[:3]
        if rank == 2 and x[0] > 0 and x[1] > 0:
            # intersection exists
            intersection = hailstone.velocity.T * x[0] + hailstone.position.T
            testarea= True
            for coord in intersection:
                if coord < TESTAREA[0] or coord > TESTAREA[1]:
                    testarea = False
                    break
            if testarea:
                collisions +=1
                # print(hailstone.position , other.position, intersection, x[0], x[1])

print(collisions)