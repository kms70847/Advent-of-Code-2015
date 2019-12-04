import hashlib
import itertools

def md5(s):
    return hashlib.md5(s).hexdigest()

with open("input", "rb") as file:
    key = file.read().strip()

for size in (5,6):
    target = "0"*size
    for i in itertools.count(1):
        s = key + str(i).encode()
        if md5(s).startswith(target):
            print(i)
            break