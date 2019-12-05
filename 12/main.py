import json

def total(obj, skip_pred=lambda x: False):
    if skip_pred(obj):
        return 0
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, dict):
        return sum(total(x, skip_pred) for x in obj.keys()) + sum(total(x, skip_pred) for x in obj.values())
    elif isinstance(obj, list):
        return sum(total(value, skip_pred) for value in obj)
    elif isinstance(obj, str):
        return 0

with open("input") as file:
    d = json.load(file)

print(total(d))
print(total(d, lambda x: isinstance(x, dict) and "red" in x.values()))
