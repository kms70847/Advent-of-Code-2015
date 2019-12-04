import itertools

with open("input") as file:
    data = file.read().strip()

print(data.count("(") - data.count(")"))
x = 0
for idx, c in enumerate(data, 1):
    x += 1 if c == "(" else -1
    if x == -1:
        print(idx)
        break