import numpy as np 

with open("13/input.txt") as f:
    data = f.read()

maps = [m.split() for m in data.split("\n\n")]

# print(maps)

total = 0
for m in maps:
    map = np.zeros((len(m), len(m[0].strip())))
    
    for i, row in enumerate(m):
        for j,c in enumerate(row.strip()):
            if c == "#":
                map[i][j] = 1 
    # print(map)
    for i in range(map.shape[0] -1) :
        d = 0
        mirror = True
        while i-d >=0 and i+d+1 < map.shape[0]:
            if np.any(map[i-d] != map[i+d+1]):
                mirror = False
                break
            d+=1
        if mirror:
            total += 100*(i+1)
            # print("Mirror at row", i, i+1)
            # print("row", i, map[i])
            # print("row", i+1, map[i+1])
    for i in range(map.shape[1]-1) :
        d = 0
        mirror = True
        while i-d >=0 and i+d+1 < map.shape[1]:
            if np.any(map[:, i-d] != map[:, i+d+1]):
                mirror = False
                break
            d+=1
        if mirror:
            total += i+1
            # print("Mirror at column", i, i+1)
            # print("column", i, map[:, i])
            # print("column", i+1, map[:, i+1])

print(total)
