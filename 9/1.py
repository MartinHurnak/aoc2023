
with open("9/input.txt") as f:
    starting_sequences = f.readlines()

starting_sequences = [[int(i) for i in seq.split()] for seq in starting_sequences]


def extrapolate(seq):
    if all([i==0 for i in seq]):
        return 0
    
    diff_seq = [b-a for a,b in zip(seq, seq[1::])]
    extrapolated = extrapolate(diff_seq)
    return seq[-1] + extrapolated

res = 0
for starting_sequence in starting_sequences:
    res += extrapolate(starting_sequence)
print(res)