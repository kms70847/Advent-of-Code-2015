_cache = {}
def get_value(target):
    if target not in _cache:
        if target.isdigit():
            result = int(target)
        else:
            expr = dependencies[target]
            if len(expr) == 1: #number or single variable
                result = get_value(expr[0])
            elif len(expr) == 2: #NOT
                result = get_value(expr[1]) ^ 0xFFFF
            else: #AND or LSHIFT or RSHIFT
                if expr[1] == "AND":
                    result = get_value(expr[0]) & get_value(expr[2])
                elif expr[1] == "OR":
                    result = get_value(expr[0]) | get_value(expr[2])
                elif expr[1] == "LSHIFT":
                    result = (get_value(expr[0]) << get_value(expr[2])) & 0xFFFF
                elif expr[1] == "RSHIFT":
                    result = (get_value(expr[0]) >> get_value(expr[2])) & 0xFFFF
                else:
                    raise Exception(f"Unrecognized operator {expr[1]}")
        _cache[target] = result
            
    return _cache[target]

dependencies = {}
with open("input") as file:
    for line in file:
        expr, target = line.strip().split(" -> ")
        dependencies[target] = expr.split()

a = get_value("a")
print(a)

_cache.clear()
dependencies["b"] = [str(a)]
print(get_value("a"))