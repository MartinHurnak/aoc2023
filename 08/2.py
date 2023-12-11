from math import lcm
with open("8/input.txt") as f:
    directions, nodes = f.read().split("\n\n")

nodes_map = {}
for node in nodes.split('\n'):
    src, dst = node.replace(' ', '').split("=")
    nodes_map[src] = dst.strip('()').split(',')


directions_trans = {"R": 1, "L": 0}
directions = [directions_trans[d] for d in directions]

starting_nodes = [node for node in nodes_map.keys() if node.endswith('A')]
steps_from_a_to_z = []
for node in starting_nodes:
    current_node = node
    steps = 0
    while not current_node.endswith('Z'):
        current_node = nodes_map[current_node][directions[steps % len(directions)]]
        steps += 1
    steps_from_a_to_z.append(steps)
print(lcm(*steps_from_a_to_z))