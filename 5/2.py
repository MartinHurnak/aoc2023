with open("5/input.txt") as f:
    almanac = f.read().split("\n\n")

almanac = [a.split(":") for a in almanac]
seeds = [int(i) for i in almanac[0][1].strip().split()]
maps = {a[0]: a[1].strip().split("\n") for a in almanac[1:]}

maps_transformed = []
for mapname, map in maps.items():
    map_transformed = {}
    for maprow in map:
        dest, src, rng = [int(i) for i in maprow.split()]
        map_transformed[(src, src + rng - 1)] = dest
    maps_transformed.append(map_transformed)


min_location = None


def resolve_range(rng, map, depth=0):
    new_ranges = []
    if rng[1] < rng[0]:
        return []
    for src, dst in map.items():
        if src[0] <= rng[1] or src[1] >= rng[0]:
            offset = rng[0] - src[0]
            if src[0] <= rng[0] and rng[1] <= src[1]:
                new_ranges.append((dst + offset, dst + offset + (rng[1] - rng[0])))
                return new_ranges
            elif rng[0] <= src[0] and src[1] <= rng[1]:
                new_ranges += resolve_range((rng[0], src[0] - 1), map)
                new_ranges.append((dst, dst + (src[1] - src[0])))
                new_ranges += resolve_range((src[1] + 1, rng[1]), map)
                return new_ranges
            elif src[0] <= rng[0] <= src[1]:
                new_ranges.append((dst + offset, dst + offset + (src[1] - rng[0])))
                new_ranges += resolve_range((src[1] + 1, rng[1]), map)
                return new_ranges
            elif src[0] <= rng[1] <= src[1]:
                new_ranges.append((dst, dst + (rng[1] - src[0])))
                new_ranges += resolve_range((rng[0], src[0] - 1), map)
                return new_ranges
    return [rng]


for seed_low, rng in zip(seeds[::2], seeds[1::2]):
    print("Processing range", (seed_low, seed_low + rng))

    ranges = [(seed_low, seed_low + rng)]
    new_ranges = []
    for mapname, map in zip(maps.keys(), maps_transformed):
        for rg in ranges:
            new_ranges += resolve_range(rg, map)
        ranges = new_ranges
        new_ranges = []

    for rg in ranges:
        if min_location is None or rg[0] < min_location:
            min_location = rg[0]

print(min_location)
