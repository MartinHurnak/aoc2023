from collections import Counter

with open("7/input.txt") as f:
    lines = f.readlines()


class Hand:
    scores = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}

    def __init__(self, cards: str, bid: str):
        self.cards = cards
        self.bid = int(bid)
        self.counts = None
        self.jokers = None

    def __eq__(self, other) -> bool:
        return self.cards == other.cards

    def __lt__(self, other) -> bool:
        lhs, rhs = self.power(), other.power()
        if lhs != rhs:
            return lhs < rhs
        else:
            for i in range(len(self.cards)):
                if self.card_score(i) == other.card_score(i):
                    continue
                else:
                    return self.card_score(i) < other.card_score(i)

    def card_score(self, index):
        card = self.cards[index]
        if card.isdigit():
            return int(card)
        else:
            return self.scores[card]

    def power(self):
        if self.counts == None:
            self.counts = Counter(self.cards)
            self.jokers = self.counts.pop("J", 0)

        best = self.counts.most_common(2)
        if self.jokers == 5:
            return 7
        if best[0][1] + self.jokers == 5:
            return 7
        if best[0][1] + self.jokers == 4:
            return 6
        if best[0][1] == 3:
            if best[1][1] == 2:  # full-house
                return 5
            return 4  # three
        if best[0][1] == 2:
            if best[1][1] == 2:
                if self.jokers == 1:  # 2+2+J full-house
                    return 5
                return 3  # two-pairs
            if self.jokers == 1:  # three
                return 4
            return 2  # pair
        if best[0][1] == 1:
            if self.jokers == 2:  # three
                return 4
            elif self.jokers == 1:  # pair
                return 2
            return 1


hands = [Hand(*line.split()) for line in lines]


hands.sort()
print([h.cards for h in hands])
print(sum([h.bid * (i + 1) for i, h in enumerate(hands)]))
