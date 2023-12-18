with open("12/input.txt") as f:
    data = f.readlines()

springs = [row.split() for row in data]
# print(springs)


def validate(springs, sequences):
    damaged = 0
    groupindex = 0
    for spring in springs:
        if spring == "#":
            damaged +=1
        if spring == '.':
            if damaged > 0:
                if damaged != sequences[groupindex]:
                    #print("Error:", springs, sequences)
                    return False
                groupindex +=1
                damaged = 0

    if damaged > 0:
        if groupindex != len(sequences) - 1 or damaged != sequences[groupindex]:
            #print("Error:", springs, sequences)
            return False
    else:
        if groupindex < len(sequences):
            return False
    print(groupindex, damaged)
    return True


def count_damaged(springs, sequences, index=0, groupindex=0, damaged=0, help=""):
    if index >= len(springs):
        if damaged == 0 and groupindex >= len(sequences):
            # print("C1", help)

            return 1
        elif groupindex == len(sequences)-1 and damaged == sequences[groupindex]:
            # print("C2", help)

            return 1
        else:
            if validate(help, sequences):
                raise Exception
            return 0

    valid = 0
    for i, spring in enumerate(springs[index:]):
        if groupindex >= len(sequences) and damaged > 0:
            if validate(help, sequences):
                raise Exception
            return 0
        if spring == ".":
            if damaged > 0:
                if damaged != sequences[groupindex]:
                    return 0

                groupindex += 1
            damaged = 0
            help += "."
            continue
        if spring == "#":
            damaged += 1
            help += "#"
            continue
        if spring == "?":
            if damaged > 0 and damaged > sequences[groupindex]:
                return 0
            elif damaged > 0 and damaged == sequences[groupindex]:
                valid += count_damaged(
                    springs,
                    sequences,
                    index + i + 1,
                    groupindex + 1,
                    0,
                    help=help + ".",
                )
            else:
                if damaged == 0:
                    valid += count_damaged(
                        springs, sequences, index + i + 1, groupindex, 0, help=help + "."
                    )
                valid += count_damaged(
                    springs,
                    sequences,
                    index + i + 1,
                    groupindex,
                    damaged + 1,
                    help=help + "#",
                )
            return valid
    
    if damaged > 0:
        if groupindex != len(sequences) - 1 or damaged != sequences[groupindex]:
            #print("Error:", springs, sequences)
            return 0
    else:
        if groupindex < len(sequences):
            return 0

    return 1

total = 0
for springsrow in springs:
    seq = [int(i) for i in springsrow[1].split(",")]
    total += count_damaged(springsrow[0], seq)
print(total)