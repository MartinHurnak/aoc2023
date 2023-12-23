from functools import cache

with open("12/input.txt") as f:
    data = f.readlines()

springs = [row.split() for row in data]


@cache
def count_damaged(springs, sequences, index=0, groupindex=0, damaged=0):
    if index >= len(springs):
        if damaged == 0 and groupindex >= len(sequences):
            return 1
        elif groupindex == len(sequences) - 1 and damaged == sequences[groupindex]:
            return 1
        else:
            return 0

    valid = 0
    for i, spring in enumerate(springs[index:]):
        if groupindex >= len(sequences) and damaged > 0:
            return 0
        if spring == ".":
            if damaged > 0:
                if damaged != sequences[groupindex]:
                    return 0

                groupindex += 1
            damaged = 0
            continue
        if spring == "#":
            damaged += 1
            continue
        if spring == "?":
            if damaged > 0 and damaged > sequences[groupindex]:
                return 0
            elif damaged > 0 and damaged == sequences[groupindex]:
                valid += count_damaged(
                    springs, sequences, index + i + 1, groupindex + 1, 0
                )
            else:
                if damaged == 0:
                    valid += count_damaged(
                        springs, sequences, index + i + 1, groupindex, 0
                    )
                valid += count_damaged(
                    springs, sequences, index + i + 1, groupindex, damaged + 1
                )
            return valid

    if damaged > 0:
        if groupindex != len(sequences) - 1 or damaged != sequences[groupindex]:
            # print("Error:", springs, sequences)
            return 0
    else:
        if groupindex < len(sequences):
            return 0

    return 1


total = 0
for row, springsrow in enumerate(springs):
    print(row)
    seq = tuple([int(i) for i in springsrow[1].split(",")])
    total += count_damaged("?".join([springsrow[0]] * 5), seq * 5)
print(total)
