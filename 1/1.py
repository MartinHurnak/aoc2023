with open("1/input.txt") as f:   
    data =  f.readlines()

sum = 0
for line in data:
    first, last = None, None
    for c in line:
        if c.isdigit():
            first = first or c
            last = c
    sum += int(first+last)
print (sum)