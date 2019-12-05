import itertools
import re
import collections

names = set()
costs = collections.defaultdict(int)
with open("input") as file:
    for line in file:
        a, direction, amount, b = re.match("(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)", line).groups()
        sign = 1 if direction == "gain" else -1
        names.add(a)
        names.add(b)
        costs[a,b] = int(amount)*sign

for part in (1,2):
    if part == 2:
        names.add("Me")
    seq = []
    for order in itertools.permutations(names):
        cost = sum(costs[order[i], order[i-1]] + costs[order[i-1], order[i]] for i in range(len(order)))
        seq.append(cost)

    print(max(seq))