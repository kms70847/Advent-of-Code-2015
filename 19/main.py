import collections

def replace_each(s, old, new):
    return [replace_once(s, old, new, i+1) for i in range(s.count(old))]

def replace_once(s, old, new, count):
    assert "~" not in s
    assert s.count(old) >= count
    return s.replace(old, "~", count).replace("~", old, count-1).replace("~", new)

d = collections.defaultdict(list)
with open("input") as file:
    for line in file:
        line = line.strip()
        if not line: continue
        if " => " in line:
            key, value = line.split(" => ")
            d[key].append(value)
        else:
            s = line

#part 1
print(len({x for k, vals in d.items() for val in vals for x in replace_each(s, k, val)}))

#part 2
d = {value: key for key, values in d.items() for value in values}

count = 0
while s != "e":
    """
    Try to perform replacements until `s` reaches the starting state.
    There's no reason to expect this to consistently work,
    since it could easily end in a blind alley where no replacements can be made.
    And in fact, the first three candidate-choosing criteria I tried did exactly that.
    But picking the rightmost candidate works on my specific input, so... Good enough.
    """
    candidates = [k for k in d.keys() if k in s]
    k = max(candidates, key=s.index)
    s = s.replace(k, d[k], 1)
    count += 1
print(count)