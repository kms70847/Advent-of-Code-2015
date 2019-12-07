import itertools
import copy

def choose(seq, min_items, max_items):
    for i in range(min_items, 1+max_items):
        yield from itertools.combinations(seq, i)

boss = {}
with open("input") as file:
    for line in file:
        k,v = line.split(": ")
        boss[k.lower()] = int(v)


shop = {}
with open("shop") as file:
    for raw_category in file.read().split("\n\n"):
        lines = raw_category.split("\n")
        category = []
        for line in lines[1:]:
            name, cost, damage, armor = filter(None, line.split("  "))
            category.append({
                "name": name,
                "cost": int(cost),
                "damage": int(damage),
                "armor": int(armor)
            })

        shop[lines[0].split(":")[0]] = category

def iter_buildouts():
    for weapons in choose(shop["Weapons"], 1, 1):
        for armors in choose(shop["Armor"], 0, 1):
            for rings in choose(shop["Rings"], 0, 2):
                yield weapons + armors + rings

def does_player_win(buildout):
    player = {"damage": 0, "armor": 0, "hit points": 100}
    for item in buildout:
        player["damage"] += item["damage"]
        player["armor"] += item["armor"]
    
    agents = [player, copy.deepcopy(boss)]
    for i in itertools.count():
        a = agents[i%2]
        b = agents[(i+1)%2]
        b["hit points"] = b["hit points"] - max(1, a["damage"] - b["armor"])
        if b["hit points"] <= 0:
            return (i%2) == 0

def cost(buildout):
    return sum(item["cost"] for item in buildout)

print(cost(min((b for b in iter_buildouts() if does_player_win(b)), key=cost)))
print(cost(max((b for b in iter_buildouts() if not does_player_win(b)), key=cost)))
