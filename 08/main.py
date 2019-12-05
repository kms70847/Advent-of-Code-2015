def decode(s):
    assert s.startswith('"') and s.endswith('"')
    result = []
    i = 1
    while i < len(s)-1:
        if s[i] == "\\":
            if s[i+1] == '"' or s[i+1] == "\\":
                result.append(s[i+1])
                i += 2
            elif s[i+1] == "x":
                ordinal = int(s[i+2:i+4], 16)
                result.append(ordinal)
                i += 4
            else:
                raise Exception(f"Unrecognized esacpe code {repr(s[i+1])}")
        else:
            result.append(s[i])
            i += 1
    return result

def encode(s):
    result = ['"']
    for c in s:
        if c == '"':
            result.extend(["\\", '"'])
        elif c == "\\":
            result.extend(["\\", "\\"])
        else:
            result.append(c)
    result.append('"')
    return result

with open("input") as file:
    inputs = [line.strip() for line in file]

print(sum(len(s) for s in inputs) - sum(len(decode(s)) for s in inputs))
print(sum(len(encode(s)) for s in inputs) - sum(len(s) for s in inputs))
