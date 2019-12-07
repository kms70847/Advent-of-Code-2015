import itertools

def selections(seq):
    for mask in itertools.product((False, True), repeat=len(seq)):
        yield [item for x, item in zip(mask, seq) if x]

with open("input") as file:
    seq = list(map(int, file.read().split()))

target = 150

candidates = [item for item in selections(seq) if sum(item) == target]
print(len(candidates))

size = len(min(candidates, key=len))
print(sum(1 for item in candidates if len(item) == size))