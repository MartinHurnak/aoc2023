from collections import namedtuple

with open("15/input.txt") as f:
    data = f.read()
sequences = data.strip("\n").split(",")

boxes = [[] for _ in range(256)]


def hash_sequence(sequence):
    hash = 0
    for c in sequence:
        hash = ((hash + ord(c)) * 17) % 256
    return hash


for seq in sequences:
    if "-" in seq:
        label = seq.split("-")[0]
        box_index = hash_sequence(label)
        boxes[box_index] = [l for l in boxes[box_index] if l[0] != label]
    elif "=" in seq:
        lens = seq.split("=")
        box_index = hash_sequence(lens[0])
        replaced = False
        for l in boxes[box_index]:
            if l[0] == lens[0]:
                l[1] = lens[1]
                replaced = True
                break
        if not replaced:
            boxes[box_index].append(lens)

focus_power = 0
for box_index, box in enumerate(boxes):
    if box:
        print(box_index, box)
    for slot_index, slot in enumerate(box):
        focus_power += (1 + box_index) * (1 + slot_index) * int(slot[1])
print(focus_power)
