import re

def try_ints(seq):
    results = []
    for item in seq:
        try:
            results.append(int(item))
        except ValueError:
            results.append(item)
    return results

commands = []
with open("input") as file:
    for line in file:
        commands.append(try_ints(re.match("(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)", line).groups()))

operations = {
    1: {
        "turn on": lambda x: 1,
        "turn off": lambda x: 0,
        "toggle": lambda x: 1-x
    },
    2: {
        "turn on": lambda x: x+1,
        "turn off": lambda x: 0 if x == 0 else x-1,
        "toggle": lambda x: x+2
    }
}

for part in (1,2):
    field = [[0]*1000 for _ in range(1000)]
    for op, left, top, right, bottom in commands:
        for i in range(left, right+1):
            for j in range(top, bottom+1):
                field[j][i] = operations[part][op](field[j][i])
    print(sum(sum(row) for row in field))