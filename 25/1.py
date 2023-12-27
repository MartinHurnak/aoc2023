import networkx as nx

with open("25/input.txt") as f:
    data = f.readlines()

G = nx.Graph()
for line in data:
    name, connections = line.strip().split(": ")
    for conn in connections.split():
        G.add_edge(name, conn, capacity=1.0)

for i, c1 in enumerate(G.nodes):
    for c2 in list(G.nodes)[i+1:]:
        value, partition = nx.minimum_cut(G, c1, c2)
        if value == 3:
            g1, g2 = partition
            # print(partition, c1, c2, value)
            print(len(g1) * len(g2))
            exit()
