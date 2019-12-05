import itertools

def tick(s):
    result = []
    for k, v in itertools.groupby(s):
        result.extend([str(len(list(v))), k])
    return "".join(result)

with open("input") as file:
    s = file.read().strip()

for _ in range(40):
    s = tick(s)

print(len(s))

for _ in range(10):
    s = tick(s)

print(len(s))