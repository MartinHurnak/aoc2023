with open("14/input.txt") as f:
    platform = f.readlines()

platform = [row.strip() for row in platform]
maxload = len(platform)

total_load = 0
for col_index in range(len(platform[0])):
    index_free = 0
    for row_index, row in enumerate(platform):
        if row[col_index] == "#":
            index_free = row_index + 1
        elif row[col_index] == "O":
            total_load += maxload - index_free
            # print("Rock at", col_index, row_index, "rolls to", index_free, "load", maxload - index_free)
            index_free += 1
            
print(total_load) 