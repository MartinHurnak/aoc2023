from ast import literal_eval
with open("8/input.txt") as f:
    directions, nodes = f.read().split("\n\n")

nodes_map = {}
for node in nodes.split('\n'):
    src, dst = node.replace(' ', '').split("=")
    nodes_map[src] = dst.strip('()').split(',')


directions_trans = {"R": 1, "L": 0}
directions = [directions_trans[d] for d in directions]

current_node = "AAA"
steps = 0
while current_node != "ZZZ":
    current_node = nodes_map[current_node][directions[steps % len(directions)]]
    steps += 1
print(steps)