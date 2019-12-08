import math

def masks(size, num_trues):
    assert size >= num_trues
    if size == num_trues:
        yield [True] * size
        return
    if num_trues == 0:
        yield [False] * size
        return

    for x in masks(size-1, num_trues):
        yield [False] + x
    for x in masks(size-1, num_trues-1):
        yield [True] + x

with open("input") as file:
    data = [int(x) for x in file.read().split()]

for part in (1,2):
    bins = 3 if part == 1 else 4
    candidates = []
    found = False
    for i in range(1, len(data)):
        if found: break
        for mask in masks(len(data), i):
            seq = [x for x,b in zip(data, mask) if b]
            if sum(seq) == sum(data) // bins:
                candidates.append(seq)
                found = True
    best = min(candidates, key=math.prod)
    print(math.prod(best))