with open("6/input.txt") as f:
    lines = f.readlines()

times = [int(i) for i in lines[0].split(":")[1].strip().split()]
distances = [int(i) for i in lines[1].split(":")[1].strip().split()]
print(times, distances)


res = 1
for t, d in zip(times, distances):
    p = 0
    for v in range(t+1):
        if v*(t-v) > d:
            p+=1
            print(t, d, v,  v*(t-v))
    res *= p
print(res)