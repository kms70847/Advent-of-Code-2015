import re

reindeers = []
with open("input") as file:
    for line in file:
        reindeers.append([int(x) for x in re.findall("\d+", line)])

positions = [0] * len(reindeers)
scores = [0] * len(reindeers)

for t in range(2503):
    for idx, (speed, fly_time, rest_time) in enumerate(reindeers):
        positions[idx] += speed if t % (fly_time+rest_time) < fly_time else 0
    for idx in range(len(positions)):
        if positions[idx] == max(positions):
            scores[idx] += 1

print(max(positions))
print(max(scores))