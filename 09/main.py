import re
import itertools

distances = {}
places = set()
with open("input") as file:
    for line in file:
        a,b, dist = re.match("(\w+) to (\w+) = (\d+)", line).groups()
        dist = int(dist)
        distances[a,b] = dist
        distances[b,a] = dist
        places.add(a)
        places.add(b)

route_lengths = []
for route in itertools.permutations(places):
    length = sum(distances.get((route[i], route[i+1]), float("inf")) for i in range(len(route)-1))
    if length != float("inf"):
        route_lengths.append(length)

print(min(route_lengths))
print(max(route_lengths))
