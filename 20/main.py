import itertools

with open("input") as file:
    target = int(file.read())
    
for part in (1,2):
    multiplier = 10 if part == 1 else 11
    sieve = [0] * (1 + target//10)
    for i in range(1, len(sieve)):
        for j in range(i, len(sieve), i):
            if part == 2 and (j / i) == 50: break
            sieve[j] += i*multiplier
    print(next(idx for idx, item in enumerate(sieve) if item >= target))