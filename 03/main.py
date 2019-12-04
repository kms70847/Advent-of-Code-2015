from geometry import Point

deltas = {"^": Point(0,-1), "v": Point(0,1), "<": Point(-1,0), ">": Point(1,0)}

def get_path(seq):
    p = Point(0,0)
    path = [p]
    for c in seq:
        p += deltas[c]
        path.append(p)
    return path

with open("input") as file:
    data = file.read()

print(len(set(get_path(data))))

a = [data[i] for i in range(0, len(data), 2)]
b = [data[i] for i in range(1, len(data), 2)]
print(len(set(get_path(a)) | set(get_path(b))))