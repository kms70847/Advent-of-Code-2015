def is_nice(s, part):
    if part == 1:
        return sum(s.count(c) for c in "aeiou") >= 3 \
            and any(s[i-1] == s[i] for i in range(1, len(s))) \
            and not any(x in s for x in ("ab", "cd", "pq", "xy"))
    else:
        pairs = {s[i:i+2] for i in range(len(s)-1)}
        return any(s.count(pair) >= 2 for pair in pairs) \
            and any(s[i-2] == s[i] for i in range(2, len(s)))

with open("input") as file:
    data = [line.strip() for line in file]

for part in (1,2):
    print(sum(1 for s in data if is_nice(s, part)))
