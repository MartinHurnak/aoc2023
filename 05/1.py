with open("5/input.txt") as f:
    almanac = f.read().split("\n\n")

almanac = [a.split(":") for a in almanac]
seeds = almanac[0][1].strip().split()
maps = {a[0]: a[1].strip().split("\n") for a in almanac[1:]}


maps_transformed = []
for mapname, map in maps.items():
    map_transformed = {}
    for maprow in map:
        dest, src, rng = [int(i) for i in maprow.split()]
        map_transformed[(src, src + rng - 1)] = dest
    maps_transformed.append(map_transformed)

min_location = None
for seed in seeds:
    value = int(seed)
    for map in maps_transformed:
        nextmap = False
        for src, dst_low in map.items():
            src_low, src_high = src
            if src_low <= value <= src_high:
                value = dst_low + (value - src_low)
                nextmap = True
                break
        if nextmap:
            continue

    if min_location is None or value < min_location:
        min_location = value

print(min_location)
