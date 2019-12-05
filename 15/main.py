import math

def ways(total, groups):
    if groups == 1:
        yield [total]
    else:
        for i in range(0, total+1):
            for right in ways(total-i, groups-1):
                yield [i] + right

ingredients = []
with open("input") as file:
    for line in file:
        name, qualities = line.strip().split(": ")
        d = {"name": name}
        for s in qualities.split(", "):
            k,v = s.split()
            d[k] = int(v)
        ingredients.append(d)

recipes = []
for ingredient_quantities in ways(100, len(ingredients)):
    recipe = {"capacity": 0, "durability": 0, "flavor": 0, "texture": 0, "calories": 0}
    for qty, ingredient in zip(ingredient_quantities, ingredients):
        for k in recipe.keys():
            recipe[k] += qty * ingredient[k]
    recipe["score"] = math.prod(max(0, recipe[k]) for k in "capacity durability flavor texture".split())
    recipes.append(recipe)

print(max(recipe["score"] for recipe in recipes))
print(max(recipe["score"] for recipe in recipes if recipe["calories"] == 500))