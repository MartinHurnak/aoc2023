import os
for i in range(6, 25):
    dirname = str(i)
    os.makedirs(dirname,exist_ok=True)
    for filename in ["1.py", "2.py", "test.txt", "input.txt"]:
        with open(os.path.join(dirname, filename), "w"):
            pass