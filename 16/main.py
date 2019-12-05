import operator

sues = []
with open("input") as file:
    for line in file:
        name, attrs = line.strip().split(": ",1)
        d = {"name": name.split()[1]}
        for s in attrs.split(", "):
            k,v = s.split(": ")
            d[k] = int(v)
        sues.append(d)

target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

comparators = {k: operator.eq for k in target.keys()}

for part in (1,2):
    if part == 2:
        comparators["cats"] = operator.gt
        comparators["trees"] = operator.gt
        comparators["pomeranians"] = operator.lt
        comparators["goldfish"] = operator.lt
    for sue in sues:
        if all(k not in target or comparators[k](v, target[k]) for k,v in sue.items()):
            break
    else:
        raise Exception("Not found")
    print(sue["name"])