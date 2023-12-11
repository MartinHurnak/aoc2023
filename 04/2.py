with open("4/input.txt") as f:
    cards = f.readlines()


card_counts = [1] * len (cards)
for i, card in enumerate(cards):
    winning, actual =  card.split(":")[1].split("|")
    winning = set(winning.strip().split())
    actual = set(actual.strip().split())
    intersect = winning.intersection(actual)
    
    if intersect:
        for j in range(i+1, min(i+1+len(intersect), len(card_counts))):
            card_counts[j] += card_counts[i]
print(sum(card_counts))