valid_letters = "abcdefghjkmnpqrstuvwxyz"
successor = {valid_letters[i]: valid_letters[i+1] for i in range(len(valid_letters)-1)}

def increment(s):
    def increment_(c):
        if c == "z":
            return "a", True
        else:
            return successor[c], False

    result = []
    for c in reversed(s):
        c, carry = increment_(c)
        result.append(c)
        if not carry: 
            break
    else:
        raise Exception("can't change the size of s")
    result.append(s[:-len(result)])
    return "".join(reversed(result))

def is_valid(s):
    def is_run(seq):
        seq = [ord(c) for c in seq]
        return all(item == seq[0] + idx for idx, item in enumerate(seq))
    if not any(is_run(s[i:i+3]) for i in range(len(s)-3)):
        return False

    overlaps = set()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            overlaps.add(s[i:i+2])
    if not sum(s.count(overlap) for overlap in overlaps) >= 2:
        return False
    return True

with open("input") as file:
    s = file.read().strip()

answers = []
while True:
    s = increment(s)
    if is_valid(s):
        print(s)
        answers.append(s)
        if len(answers) == 2:
            break
