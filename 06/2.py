with open("6/input.txt") as f:
    lines = f.readlines()

t = int(lines[0].split(":")[1].replace(' ', ''))
d = int(lines[1].split(":")[1].replace(' ', ''))


res = 0
for v in range(t+1):
    if v*(t-v) > d:
        res+=1
        # print(t, d, v,  v*(t-v))

print(res)