with open("4/input.txt") as f:
    cards = f.readlines()

sum = 0
for card in cards:
    winning, actual = card.split(":")[1].split("|")
    winning = set(winning.strip().split())
    actual = set(actual.strip().split())
    intersect = winning.intersection(actual)
    if intersect:
        sum += 2 ** (len(intersect) - 1)
print(sum)
